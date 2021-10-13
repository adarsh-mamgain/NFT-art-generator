"""
This is the main module to create NFTs. Run 'python3 main.py' command to generate NFTs
"""

import random
import datetime
import json
import os
import shutil
import hashlib
from PIL import Image
import layers
import config

dnaList = []


def get_rarity():
    """Generates the NFTs rarity"""
    total_sum = 0
    rarity_percent = []
    rarity_percent = list(map(int, input("Enter rarity percent ↓↓↓\n(Original, Rare, Super rare): ").split()))
    if not rarity_percent:
        print("No input provided, default rarity percent is used Original: 50 Rare: 30 Super rare: 20")
        for i in config.rarity_weights:
            rarity_percent.append(config.rarity_weights[i]["count"])
    for i in rarity_percent:
        total_sum += i
    if (len(rarity_percent) == len(list(dict(config.rarity_weights)))and total_sum == 100):
        for i, j in zip(config.rarity_weights, rarity_percent):
            config.rarity_weights[i]["count"] = int(layers.editionSize * j / 100)
        if layers.editionSize % 2 != 0:
            config.rarity_weights["original"]["count"] += 1
        return config.rarity_weights
    else:
        print("RERUN")
        return get_rarity()


def is_dna_unique(_dna_id):
    """Checks if the DNA is unique"""
    dna = "".join(map(str, _dna_id))
    if dna in dnaList:
        return False
    dnaList.append(dna)
    return True


def create_dna(_rarity_weights):
    """Generates the NFTs DNA"""
    random_dna = []
    element_list = []
    layer_list = []
    for layer in layers.races["mandalorian"]["layers"]:
        get_all_images = []
        rarity = random.choice(_rarity_weights)
        for rare in layers.races["mandalorian"]["layers"][layer]["elements"][rarity]["list"]:
            get_all_images.append(rare)
        element = random.choice(get_all_images)
        element_list.append(element)
        layer_list.append(layer)
        random_dna.append(layers.races["mandalorian"]["layers"][layer]["layer_id"])
        random_dna.append(layers.races["mandalorian"]["layers"][layer]["elements"][rarity]["rarity_id"])
        random_dna.append(element["element_id"])
    return element_list, layer_list, random_dna


def create_image(_images_path, _edition_count):
    """Creates the NFT images"""
    for path in _images_path:
        try:
            background = Image.open(f"{config.IMAGES_DIRECTORY}/{_edition_count}.png")
            foreground = Image.open(path)
            Image.alpha_composite(background.convert("RGBA"), foreground.convert("RGBA")).save(f"{config.IMAGES_DIRECTORY}/{_edition_count}.png")
        except FileNotFoundError:
            background = (Image.open(path).convert("RGBA").save(f"{config.IMAGES_DIRECTORY}/{_edition_count}.png"))
    print("Built: ", _edition_count)


def clear_data():
    """Deletes the 'build' directory and all of it's content + metadata.json"""
    if os.path.exists(config.OUTPUT_DIRECTORY):
        shutil.rmtree(config.OUTPUT_DIRECTORY)
    os.mkdir(config.OUTPUT_DIRECTORY)
    os.mkdir(config.IMAGES_DIRECTORY)
    os.mkdir(config.METADATA_DIRECTORY)
    data = []
    with open("metadata.json", "r+", encoding="utf-8") as file:
        file.truncate()
        file.seek(0)
        json.dump(data, file)


# ! Finalize the Metadata type and requirements
def save_metadata(_edition_count, _dna, images):
    """This function creates the required json files and saves the metadata"""
    data = {
        "name": f"#{_edition_count}",
        "dna": _dna,
        "dnaHash": hashlib.sha1(_dna.encode()).hexdigest().upper(),
        "date": str(datetime.datetime.utcnow()),
        "description": config.DESCRIPTION,
        "image": f"{config.BASE_IMAGE_URI}/{_edition_count}.png",
        "attributes": [],
    }
    for image in images:
        data["attributes"].append(image)

    with open(f"{config.METADATA_DIRECTORY}/{_edition_count}.json", "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4)

    with open("metadata.json", "r+", encoding="utf-8") as file:
        file_data = json.load(file)
        file_data.append(data)
        file.seek(0)
        json.dump(file_data, file)
    return data


# ! CREATE SMART CONTRACTS
def main():
    """The main function of the program for creating the required NFTs"""
    get_rarity()
    edition_count = 1
    print("Edition size: ", layers.editionSize)
    print("Creating your NFTs ...")
    clear_data()
    while edition_count <= layers.editionSize:
        while True:
            rare = random.choice(list(config.rarity_weights))
            if config.rarity_weights[rare]["count"] > 0:
                break

        element_list, layer_list, dna_id = create_dna(config.rarity_weights[rare]["list"])
        dna = "".join(map(str, dna_id))
        if is_dna_unique(dna_id):
            config.rarity_weights[rare]["count"] -= 1
            images = []
            images_path = []
            for selected_element, selected_layer in zip(element_list, layer_list):
                metadata = {
                    "trait_type": selected_layer,
                    "value": selected_element["name"],
                }
                images.append(metadata)
                location = selected_element["location"]
                images_path.append(location)

            try:
                save_metadata(edition_count, dna, images)
                create_image(images_path, edition_count)
                edition_count += 1
            except RuntimeError:
                print("Save_metadata or Create_image is not working :(")
        else:
            print("DNA exists: ", dna)


if __name__ == "__main__":
    main()
