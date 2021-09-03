import pathlib

# todo Rename layers with rarity

directory = "./input/"
rarity = {
  "": "original",
  "_r": "rare",
  "_sr": "super rare"
}

def cleanName(fileName):
  sliced = fileName[:-4]
  for i in rarity:
    if i in sliced:
      name = sliced.replace(i, '')
  return name

def addRarity(fileName):
  for i in rarity:
    if i in fileName:
      rare = rarity[i]
  return rare

def getElement(dir):
  counter = 0
  elements = []
  for path in pathlib.Path(dir).iterdir():
    if path.is_file():
      counter += 1
      value = {
        "id": counter,
        "name": cleanName(path.name),
        "filename": path.name,
        "location": f"{dir}{path.name}",
        "rarity": addRarity(path.name)
      }
      elements.append(value)
  return elements

'''
Type layers in the order of their apperance on 
the output image where, layer_id = 1 means bottom most layer 
and the biggest numbered layer_id (eg: 5) is the top most layer
'''

layers = {
  "backgrond": {
    "layer_id": 1,
    "elements": getElement(f"{directory}background/"),
  },
  "armour": {
    "layer_id": 2,
    "elements": getElement(f"{directory}armour/"),
  },
  "pattern": {
    "layer_id": 3,
    "elements": getElement(f"{directory}pattern/"),
  },
  "helmet": {
    "layer_id": 4,
    "elements": getElement(f"{directory}helmet/"),
  },
  "cheek": {
    "layer_id": 5,
    "elements": getElement(f"{directory}cheek/"),
  }
}
