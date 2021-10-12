"""This module provides layers in formatted manner"""

import pathlib
import config

editionSize = int(input("Enter the edition size: "))


def get_element(_layer_path):
    """Returns formatted file name"""
    counter = 0
    elements_list = []
    for element in pathlib.Path(_layer_path).iterdir():
        if element.is_file() and not element.name.startswith("."):
            value = {
                "element_id": counter,
                "name": element.name[:-4],
                "location": f"{_layer_path}/{element.name}",
            }
            elements_list.append(value)
            counter += 1
    return elements_list


# Type layers in the order of their apperance on
# the output image where, layer_id = A means bottom most layer
# and the biggest numbered layer_id (eg: E) is the top most layer

races = {
    "mandalorian": {
        "name": "Mandalorian",
        "layers": {
            "background": {
                "layer_id": "A",
                "elements": {
                    "original": {
                        "rarity_id": 0,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/background/original"),
                    },
                    "rare": {
                        "rarity_id": 1,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/background/rare"),
                    },
                    "super_rare": {
                        "rarity_id": 2,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/background/super_rare"),
                    },
                },
            },
            "armour": {
                "layer_id": "B",
                "elements": {
                    "original": {
                        "rarity_id": 0,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/armour/original"),
                    },
                    "rare": {
                        "rarity_id": 1,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/armour/rare"),
                    },
                    "super_rare": {
                        "rarity_id": 2,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/armour/super_rare"),
                    },
                },
            },
            "pattern": {
                "layer_id": "C",
                "elements": {
                    "original": {
                        "rarity_id": 0,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/pattern/original"),
                    },
                    "rare": {
                        "rarity_id": 1,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/pattern/rare"),
                    },
                    "super_rare": {
                        "rarity_id": 2,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/pattern/super_rare"),
                    },
                },
            },
            "helmet": {
                "layer_id": "D",
                "elements": {
                    "original": {
                        "rarity_id": 0,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/helmet/original"),
                    },
                    "rare": {
                        "rarity_id": 1,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/helmet/rare"),
                    },
                    "super_rare": {
                        "rarity_id": 2,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/helmet/super_rare"),
                    },
                },
            },
            "cheek": {
                "layer_id": "E",
                "elements": {
                    "original": {
                        "rarity_id": 0,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/cheek/original"),
                    },
                    "rare": {
                        "rarity_id": 1,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/cheek/rare"),
                    },
                    "super_rare": {
                        "rarity_id": 2,
                        "list": get_element(f"{config.INPUT_DIRECTORY}/cheek/super_rare"),
                    },
                },
            },
        },
    }
}
