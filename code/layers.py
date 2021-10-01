import config
import pathlib

editionSize = int(input("Enter the edition size: "))

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
            "list": getElement(f"{config.inputDirectory}/background/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{config.inputDirectory}/background/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{config.inputDirectory}/background/super_rare")
          }
        }
      },
      "armour": {
        "layer_id": 'B',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{config.inputDirectory}/armour/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{config.inputDirectory}/armour/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{config.inputDirectory}/armour/super_rare")
          }
        }
      },
      "pattern": {
        "layer_id": 'C',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{config.inputDirectory}/pattern/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{config.inputDirectory}/pattern/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{config.inputDirectory}/pattern/super_rare")
          }
        }
      },
      "helmet": {
        "layer_id": 'D',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{config.inputDirectory}/helmet/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{config.inputDirectory}/helmet/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{config.inputDirectory}/helmet/super_rare")
          }
        }
      },
      "cheek": {
        "layer_id": 'E',
        "elements": {
          "original": {
            "rarity_id": 0,
            "list": getElement(f"{config.inputDirectory}/cheek/original")
          },
          "rare":  {
            "rarity_id": 1,
            "list": getElement(f"{config.inputDirectory}/cheek/rare")
          },
          "super_rare":  {
            "rarity_id": 2,
            "list": getElement(f"{config.inputDirectory}/cheek/super_rare")
          }
        }
      }
    }
  }
}
