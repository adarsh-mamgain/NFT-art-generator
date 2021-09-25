import layers, json

def main():
  editionCount = 1
  with open("./metadata.json", "r+") as metaFile:
    data = json.load(metaFile)
    for edition in data:
      edition["image"] = f"{layers.baseImageUri}/{editionCount}.png"
      editionCount += 1
    metaFile.seek(0)
    metaFile.truncate()
    json.dump(data, metaFile)
    
  editionCount = 1
  while editionCount <= layers.editionSize:
    with open(f"./output/metadata/{editionCount}.json", "r+") as file:
      jsonData = json.load(file)
      jsonData["image"] = f"{layers.baseImageUri}/{editionCount}.png"
      file.seek(0)
      file.truncate()
      json.dump(jsonData, file, indent=4)
    editionCount += 1
  print("Regenrated files successfully :)")

if __name__ == "__main__":
  main()
