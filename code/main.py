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

dna_list = []


def is_dna_unique(_dna_id):
    """Checks if the DNA is unique"""
    dna = "".join(map(str, _dna_id))
    if dna in dna_list:
        return False
    dna_list.append(dna)
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
        json.dump(file_data, file, indent=4)
    return data


# ! CREATE SMART CONTRACTS
def main():
    """The main function of the program for creating the required NFTs"""
    edition_count = 1
    print("Edition size: ", layers.editionSize)
    print("Creating your NFTs ...")
    clear_data()
    while edition_count <= layers.editionSize:
        element_list, layer_list, dna_id = create_dna(config.rarity_weights)
        dna = "".join(map(str, dna_id))
        if is_dna_unique(dna_id):
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
