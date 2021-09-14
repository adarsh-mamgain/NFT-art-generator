from PIL import Image
import layers
import random, datetime, json

dnaList = []

def getRarity():
  sum = 0
  rarityPercent = []
  rarityPercent = list(map(int, input("Enter rarity percent ↓↓↓\n(Original, Rare, Super rare): ").split()))
  if not rarityPercent:
    print("No input provided, default rarity percent is used Original: 50 Rare: 30 Super rare: 20")
    for i in layers.rarityWeights:
      rarityPercent.append(layers.rarityWeights[i]["count"])
  for i in rarityPercent:
    sum += i
  if len(rarityPercent) == len(list(dict(layers.rarityWeights))) and sum == 100:
    for i,j in zip(layers.rarityWeights, rarityPercent):
      # ! for odd numbers add 1 more count to original

      # ! The loop fuck ups cause it should have atleast 10 edition
      # ! to make the rarityPercent work fine and find the percent but can't 
      # ! cause then the layers.rarityWeights will be in decimal for >10
      layers.rarityWeights[i]["count"] = int(layers.editionSize*j/100)
    return layers.rarityWeights
  else:
    getRarity()

def isDnaUnique(dnaId):
  dna = ''.join(map(str,dnaId))
  if dna in dnaList:
    return False
  dnaList.append(dna)
  return True

# ! make this code more clean
def createDna(rarityWeights):
  randomDna = []
  elementList = []
  rarityList = []
  layerList = []
  for layer in layers.races["mandalorian"]["layers"]:
    getAllImages = []
    rarity = random.choice(rarityWeights)
    for rare in layers.races["mandalorian"]["layers"][layer]["elements"][rarity]:
      getAllImages.append(rare)
    element = random.choice(getAllImages)
    elementList.append(element)
    rarityList.append(rarity)
    layerList.append(layer)
    randomDna.append(layers.races["mandalorian"]["layers"][layer]["layer_id"])
    randomDna.append(element["id"])
  return elementList, rarityList, layerList, randomDna

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
    "description": layers.description,
    "image": f"{layers.baseImageUri}/get/nft/#{editionCount}",
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
  getRarity()
  editionCount = 1
  print("Edition size: ", layers.editionSize)
  print("Creating your NFTs ...")
  clearMetadata()
  while editionCount <= layers.editionSize:
    while True:
      # todo make the choice more random
      rare = random.choice(list(layers.rarityWeights))
      if layers.rarityWeights[rare]["count"] > 0:
        break

    # ! make this for each race by using "raceWeights"
    # dnaId = createDna(races["mandalorian"]["layers"])
    elementList, rarityList, layerList, dnaId = createDna(layers.rarityWeights[rare]["list"])
    dna = ''.join(map(str,dnaId))
    if isDnaUnique(dnaId):
      layers.rarityWeights[rare]["count"] -= 1
      images = {}
      imagesPath = []
      # ! make this for each race by using "raceWeights"
      for selectedElement, selectedRarity, selectedLayer in zip(elementList, rarityList, layerList):
        metadata = {"name": selectedElement["name"], "rarity": selectedRarity}
        images[selectedLayer] = metadata
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