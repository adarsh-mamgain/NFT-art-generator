import pathlib

# todo Rename layers with rarity

directory = "./input"
description = "This is a test NFT project created by https://instagram.com/_adarsh_mamgain_ and https://instagram.com/shifali_amembal"
baseImageUri = "http://localhost"
startEditionFrom = 1
endEditionAt = 10
editionSize = 100

rarityWeightList = [
  {
    "value": "super_rare",
    "from": 1,
    "to": 1
  },
  {
    "value": "rare",
    "from": 2,
    "to": 4
  },
  {
    "value": "original",
    "from": 5,
    "to": editionSize
  },
]

def getElement(layerPath):
  counter = 0
  elementsList = []
  for element in pathlib.Path(layerPath).iterdir():
    if element.is_file():
      counter += 1
      value = {
        "id": counter,
        "name": element.name[:-4],
        "location": f"{layerPath}/{element.name}",
      }
      elementsList.append(value)
  return elementsList

'''
Type layers in the order of their apperance on 
the output image where, layer_id = 1 means bottom most layer 
and the biggest numbered layer_id (eg: 5) is the top most layer
'''

# ! Auto generate layers metadata while running main code instead of hardcoding
layers = {
  "backgrond": {
    "layer_id": 1,
    "elements": {
      "original": getElement(f"{directory}/background/original"),
      "rare": getElement(f"{directory}/background/rare"),
      "super_rare": getElement(f"{directory}/background/super_rare")
    }
  },
  "armour": {
    "layer_id": 2,
    "elements": {
      "original": getElement(f"{directory}/armour/original"),
      "rare": getElement(f"{directory}/armour/rare"),
      "super_rare": getElement(f"{directory}/armour/super_rare")
    }
  },
  "pattern": {
    "layer_id": 3,
    "elements": {
      "original": getElement(f"{directory}/pattern/original"),
      "rare": getElement(f"{directory}/pattern/rare"),
      "super_rare": getElement(f"{directory}/pattern/super_rare")
    }
  },
  "helmet": {
    "layer_id": 4,
    "elements": {
      "original": getElement(f"{directory}/helmet/original"),
      "rare": getElement(f"{directory}/helmet/rare"),
      "super_rare": getElement(f"{directory}/helmet/super_rare")
    }
  },
  "cheek": {
    "layer_id": 5,
    "elements": {
      "original": getElement(f"{directory}/cheek/original"),
      "rare": getElement(f"{directory}/cheek/rare"),
      "super_rare": getElement(f"{directory}/cheek/super_rare")
    }
  }
}