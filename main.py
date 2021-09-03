from PIL import Image
from layers import *
import random, datetime, json


# todo Add rarity ratio like common:rare:super_rare (20:15:5)
dnaList = []

def getRarity(editionCount):
  for rarityWeight in rarityWeightList:
    if rarityWeight["from"] <= editionCount <= rarityWeight["to"]:
      rarity = rarityWeight["value"]
  return rarity

def isDnaUnique(dnaId):
  dna = ''.join(map(str,dnaId))
  if dna in dnaList:
    return False
  dnaList.append(dna)
  return True

def createDna(layers, rarity):
  randomDna = []
  for i in layers:
    randomDna.append(int(random.uniform(0, len(layers[i]["elements"][rarity]))))
  return randomDna

def createImage(imagesPath, editionCount):
  for path in imagesPath:
    try:
      background = Image.open(f'./output/{editionCount}.png')
      foreground = Image.open(path)
      Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA')).save(f'./output/{editionCount}.png')
    except:
      background = Image.open(path).convert('RGBA').save(f'./output/{editionCount}.png')
  print("Built: ", editionCount)

def clearMetadata():
  data = []
  with open('metadata.json', 'r+') as file:
    file.truncate()
    file.seek(0)
    json.dump(data, file, indent = 2)

def saveMetadata(editionCount, dna, images):
  data = {
    "name": f"#{editionCount}",
    "edition": editionCount,
    "dna": dna,
    "date": str(datetime.datetime.utcnow()),
    "description": description,
    "image": f"{baseImageUri}/get/nft/#{editionCount}",
    "attributes": []
  }
  for i in images:
    data['attributes'].append({i: images[i]})
    
  with open('metadata.json', 'r+') as file:
    fileData = json.load(file)
    fileData.append(data)
    file.seek(0)
    json.dump(fileData, file)
  return data

def main():
  editionCount = 1
  print("Edition size: ", endEditionAt)
  print("Creating your NFTs ...")
  clearMetadata()
  while(editionCount <= int(endEditionAt)):
    rarity = getRarity(editionCount)
    dnaId = createDna(layers, rarity)
    dna = ''.join(map(str,dnaId))
    if isDnaUnique(dnaId):
      images = {}
      imagesPath = []
      for selectedElement,selectedLayer in zip(dnaId, layers):
        metadata = {"name": layers[selectedLayer]["elements"][rarity][selectedElement]["name"], "rarity": rarity}
        images[selectedLayer] = metadata
        location = layers[selectedLayer]["elements"][rarity][selectedElement]["location"]
        imagesPath.append(location)

      try:
        saveMetadata(editionCount, dna, images)
        createImage(imagesPath, editionCount)
        editionCount+=1 
      except:
        raise NotImplementedError("SaveMetadata or CreateImage is not working :(")
    else:
      print('DNA exists: ',dna)

if __name__ == "__main__":
  main()