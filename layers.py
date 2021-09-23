import pathlib

directory = "./input"
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
            "list": getElement(f"{directory}/background/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{directory}/background/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{directory}/background/super_rare")
          }
        }
      },
      "armour": {
        "layer_id": 'B',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{directory}/armour/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{directory}/armour/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{directory}/armour/super_rare")
          }
        }
      },
      "pattern": {
        "layer_id": 'C',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{directory}/pattern/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{directory}/pattern/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{directory}/pattern/super_rare")
          }
        }
      },
      "helmet": {
        "layer_id": 'D',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{directory}/helmet/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{directory}/helmet/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{directory}/helmet/super_rare")
          }
        }
      },
      "cheek": {
        "layer_id": 'E',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{directory}/cheek/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{directory}/cheek/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{directory}/cheek/super_rare")
          }
        }
      }
    }
  }
}
