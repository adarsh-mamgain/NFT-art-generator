from PIL import Image
from layers import layers
import random, datetime, json


# todo Add rarity ratio like common:rare:super_rare (20:15:5)
dnaList = []

def isDnaUnique(dnaId):
  dna = ''.join(map(str,dnaId))
  if dna in dnaList:
    return False
  dnaList.append(dna)
  return True

def createDna(layers):
  randomDna = []
  for i in layers:
    randomDna.append(int(random.uniform(0, len(layers[i]["elements"]))))
  return randomDna

def createImage(imagesPath, counter):
  for path in imagesPath:
    try:
      background = Image.open(f'./output/{counter}.png')
      foreground = Image.open(path)
      Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA')).save(f'./output/{counter}.png')
    except:
      background = Image.open(path).convert('RGBA').save(f'./output/{counter}.png')
  print("Built: ", counter)

def clearMetadata():
  data = []
  with open('metadata.json', 'r+') as file:
    file.truncate()
    file.seek(0)
    json.dump(data, file, indent = 2)

def saveMetadata(counter, dna, images):
  data = {
    "edition": counter,
    "dna": dna,
    "date": str(datetime.datetime.utcnow()),
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
  counter = 1
  edition = input("Edition: ")
  print("Creating your NFTs ...")
  clearMetadata()
  while(counter <= int(edition)):
    dnaId = createDna(layers)
    dna = ''.join(map(str,dnaId))
    if isDnaUnique(dnaId):
      images = {}
      imagesPath = []
      for selectedElement,selectedLayer in zip(dnaId, layers):
        metadata = {"name": layers[selectedLayer]["elements"][selectedElement]["name"], "rarity": layers[selectedLayer]["elements"][selectedElement]["rarity"]}
        images[selectedLayer] = metadata
        location = layers[selectedLayer]["elements"][selectedElement]["location"]
        imagesPath.append(location)

      try:
        saveMetadata(counter, dna, images)
        createImage(imagesPath, counter)
        counter+=1 
      except:
        raise NotImplementedError("SaveMetadata or CreateImage is not working :(")
    else:
      print('DNA exists: ',dna)

if __name__ == "__main__":
  main()
