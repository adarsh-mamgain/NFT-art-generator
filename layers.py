import pathlib

directory = "./input"
description = "This is a test NFT project created by https://instagram.com/_adarsh_mamgain_ and https://instagram.com/shifali_amembal"
baseImageUri = "http://localhost"

editionSize = int(input("Enter the edition size: "))

# ! Modify the code for multiple races
raceWeights = [
  {
    "value": "mandalorian",
    "from": 1,
    "to": editionSize
  },
  # {
  #   "value": "apes",
  #   "from": 2,
  #   "to": 4
  # },
  # {
  #   "value": "human",
  #   "from": 5,
  #   "to": editionSize
  # }
]

rarityWeights = {
  "original": {
    "count": 50,
    "list": ["original"]
  },
  "rare": {
    "count": 30,
    "list": ["original", "rare"]
  },
  "super_rare": {
    "count": 20,
    "list": ["original", "rare", "super_rare"]
  }
}

def getElement(layerPath):
  counter = 0
  elementsList = []
  for element in pathlib.Path(layerPath).iterdir():
    if element.is_file():
      value = {
        "id": counter,
        "name": element.name[:-4],
        "location": f"{layerPath}/{element.name}"
      }
      elementsList.append(value)
      counter += 1
  return elementsList

'''
Type layers in the order of their apperance on 
the output image where, layer_id = 0 means bottom most layer 
and the biggest numbered layer_id (eg: 4) is the top most layer
'''

races = {
  "mandalorian": {
    "name": "Mandalorian",
    "layers": {
      "background": {
        "layer_id": 0,
        "elements": {
          "original": getElement(f"{directory}/background/original"),
          "rare": getElement(f"{directory}/background/rare"),
          "super_rare": getElement(f"{directory}/background/super_rare")
        }
      },
      "armour": {
        "layer_id": 1,
        "elements": {
          "original": getElement(f"{directory}/armour/original"),
          "rare": getElement(f"{directory}/armour/rare"),
          "super_rare": getElement(f"{directory}/armour/super_rare")
        }
      },
      "pattern": {
        "layer_id": 2,
        "elements": {
          "original": getElement(f"{directory}/pattern/original"),
          "rare": getElement(f"{directory}/pattern/rare"),
          "super_rare": getElement(f"{directory}/pattern/super_rare")
        }
      },
      "helmet": {
        "layer_id": 3,
        "elements": {
          "original": getElement(f"{directory}/helmet/original"),
          "rare": getElement(f"{directory}/helmet/rare"),
          "super_rare": getElement(f"{directory}/helmet/super_rare")
        }
      },
      "cheek": {
        "layer_id": 4,
        "elements": {
          "original": getElement(f"{directory}/cheek/original"),
          "rare": getElement(f"{directory}/cheek/rare"),
          "super_rare": getElement(f"{directory}/cheek/super_rare")
        }
      }
    }
  }
}
