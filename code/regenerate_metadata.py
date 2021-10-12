"""This module regenerates the given metadata for metadata.json and all the #.json files"""

import json
import layers
import config

def main():
    """The main function of the program"""
    edition_count = 1
    with open("./metadata.json", "r+", encoding="utf-8") as meta_file:
        data = json.load(meta_file)
        for edition in data:
            edition["image"] = f"{config.BASE_IMAGE_URI}/{edition_count}.png"
            edition_count += 1
        meta_file.seek(0)
        meta_file.truncate()
        json.dump(data, meta_file)

    edition_count = 1
    while edition_count <= layers.editionSize:
        with open(f"{config.METADATA_DIRECTORY}/{edition_count}.json", "r+", encoding="utf-8") as file:
            json_data = json.load(file)
            json_data["image"] = f"{config.BASE_IMAGE_URI}/{edition_count}.png"
            file.seek(0)
            file.truncate()
            json.dump(json_data, file, indent=4)
        edition_count += 1
    print("Regenerated files successfully :)")


if __name__ == "__main__":
    main()
