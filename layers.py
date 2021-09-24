import pathlib

"""
All input and output directories for the NFTs
"""
inputDirectory = "./input"
outputDirectory = "./output"
imagesDirectory = "./output/images"
metadataDirectory = "./output/metadata"

"""
MetaData - attributes for the NFTs
"""
description = "This is a test NFT project created by https://instagram.com/_adarsh_mamgain_ and https://instagram.com/shifali_amembal"
baseImageUri = "http://localhost"

editionSize = int(input("Enter the edition size: "))

rarityWeights = {
  "original": {
    "rarity_id": 0,
    "count": 50,
    "list": ["original"]
  },
  "rare": {
    "rarity_id": 1,
    "count": 30,
    "list": ["original", "rare"]
  },
  "super_rare": {
    "rarity_id": 2,
    "count": 20,
    "list": ["original", "rare", "super_rare"]
  }
}

def getElement(layerPath):
  counter = 0
  elementsList = []
  for element in pathlib.Path(layerPath).iterdir():
    if element.is_file() and not element.name.startswith("."):
      value = {
        "element_id": counter,
        "name": element.name[:-4],
        "location": f"{layerPath}/{element.name}"
      }
      elementsList.append(value)
      counter += 1
  return elementsList

'''
Type layers in the order of their apperance on 
the output image where, layer_id = A means bottom most layer 
and the biggest numbered layer_id (eg: E) is the top most layer
'''

races = {
  "mandalorian": {
    "name": "Mandalorian",
    "layers": {
      "background": {
        "layer_id": 'A',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{inputDirectory}/background/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{inputDirectory}/background/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{inputDirectory}/background/super_rare")
          }
        }
      },
      "armour": {
        "layer_id": 'B',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{inputDirectory}/armour/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{inputDirectory}/armour/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{inputDirectory}/armour/super_rare")
          }
        }
      },
      "pattern": {
        "layer_id": 'C',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{inputDirectory}/pattern/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{inputDirectory}/pattern/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{inputDirectory}/pattern/super_rare")
          }
        }
      },
      "helmet": {
        "layer_id": 'D',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{inputDirectory}/helmet/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{inputDirectory}/helmet/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{inputDirectory}/helmet/super_rare")
          }
        }
      },
      "cheek": {
        "layer_id": 'E',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{inputDirectory}/cheek/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{inputDirectory}/cheek/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{inputDirectory}/cheek/super_rare")
          }
        }
      }
    }
  }
}
