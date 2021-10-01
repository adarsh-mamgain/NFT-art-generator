from PIL import Image
import layers, config
import random, datetime, json, os, shutil

dnaList = []

def getRarity():
  sum = 0
  rarityPercent = []
  rarityPercent = list(map(int, input("Enter rarity percent ↓↓↓\n(Original, Rare, Super rare): ").split()))
  if not rarityPercent:
    print("No input provided, default rarity percent is used Original: 50 Rare: 30 Super rare: 20")
    for i in config.rarityWeights:
      rarityPercent.append(config.rarityWeights[i]["count"])
  for i in rarityPercent:
    sum += i
  if len(rarityPercent) == len(list(dict(config.rarityWeights))) and sum == 100:
    for i,j in zip(config.rarityWeights, rarityPercent):
      config.rarityWeights[i]["count"] = int(layers.editionSize*j/100)
    if layers.editionSize % 2 != 0:
      config.rarityWeights["original"]["count"] += 1
    return config.rarityWeights
  else:
    getRarity()

def isDnaUnique(dnaId):
  dna = ''.join(map(str,dnaId))
  if dna in dnaList:
    return False
  dnaList.append(dna)
  return True

def createDna(rarityWeights):
  randomDna = []
  elementList = []
  layerList = []
  for layer in layers.races["mandalorian"]["layers"]:
    getAllImages = []
    rarity = random.choice(rarityWeights)
    for rare in layers.races["mandalorian"]["layers"][layer]["elements"][rarity]["list"]:
      getAllImages.append(rare)
    element = random.choice(getAllImages)
    elementList.append(element)
    layerList.append(layer)
    randomDna.append(layers.races["mandalorian"]["layers"][layer]["layer_id"])
    randomDna.append(layers.races["mandalorian"]["layers"][layer]["elements"][rarity]["rarity_id"])
    randomDna.append(element["element_id"])
  return elementList, layerList, randomDna

def createImage(imagesPath, editionCount):
  for path in imagesPath:
    try:
      background = Image.open(f'./output/images/{editionCount}.png')
      foreground = Image.open(path)
      Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA')).save(f'./output/images/{editionCount}.png')
    except:
      background = Image.open(path).convert('RGBA').save(f'./output/images/{editionCount}.png')
  print("Built: ", editionCount)

def clearMetadata():
  if os.path.exists(config.outputDirectory):
    shutil.rmtree(config.outputDirectory)
  os.mkdir(config.outputDirectory)
  os.mkdir(config.imagesDirectory)
  os.mkdir(config.metadataDirectory)
  data = []
  with open('metadata.json', 'r+') as file:
    file.truncate()
    file.seek(0)
    json.dump(data, file)

# ! Finalize the Metadata type and requirements
def saveMetadata(editionCount, dna, images):
  data = {
    "name": f"#{editionCount}",
    "dna": dna,
    "date": str(datetime.datetime.utcnow()),
    "description": config.description,
    "image": f"{config.baseImageUri}/{editionCount}.png",
    "attributes": []
  }
  for image in images:
    data['attributes'].append(image)
    
  with open(f"{config.metadataDirectory}/{editionCount}.json", "w") as outfile:
    json.dump(data, outfile, indent = 4)

  with open('metadata.json', 'r+') as file:
    fileData = json.load(file)
    fileData.append(data)
    file.seek(0)
    json.dump(fileData, file)
  return data

# ! CREATE SMART CONTRACTS
def main():
  getRarity()
  editionCount = 1
  print("Edition size: ", layers.editionSize)
  print("Creating your NFTs ...")
  clearMetadata()
  while editionCount <= layers.editionSize:
    while True:
      rare = random.choice(list(config.rarityWeights))
      if config.rarityWeights[rare]["count"] > 0:
        break

    elementList, layerList, dnaId = createDna(config.rarityWeights[rare]["list"])
    dna = ''.join(map(str,dnaId))
    if isDnaUnique(dnaId):
      layers.rarityWeights[rare]["count"] -= 1
      images = []
      imagesPath = []
      for selectedElement, selectedLayer in zip(elementList, layerList):
        metadata = {"trait_type": selectedLayer, "value": selectedElement["name"]}
        images.append(metadata)
        location = selectedElement["location"]
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