"""
All input and output directories for the NFTs
"""
inputDirectory = "./input"
outputDirectory = "./build"
imagesDirectory = "./build/images"
metadataDirectory = "./build/metadata"

"""
MetaData - attributes for the NFTs
"""
description = "This is a test NFT project created by https://instagram.com/_adarsh_mamgain_ and https://instagram.com/shifali_amembal"
baseImageUri = "ipfs://QmdvuRLAjd1FNPjK46tMGiRzPhjvmJagjmkK4tAYH43yYJ"

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