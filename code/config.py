"""
All input and output directories for the NFTs
"""
INPUT_DIRECTORY = "./input"
OUTPUT_DIRECTORY = "./build"
IMAGES_DIRECTORY = "./build/images"
METADATA_DIRECTORY = "./build/metadata"

"""
MetaData - attributes for the NFTs
"""
DESCRIPTION = "This is a test NFT project created by https://instagram.com/_adarsh_mamgain_ and https://instagram.com/shifali_amembal"
BASE_IMAGE_URI = "ipfs://QmdvuRLAjd1FNPjK46tMGiRzPhjvmJagjmkK4tAYH43yYJ"

rarity_weights = {
    "original": {
        "rarity_id": 0,
        "count": 50,
        "list": ["original"]
    },
    "rare": {
        "rarity_id": 1,
        "count": 30,
        "list": ["original","rare"]
    },
    "super_rare": {
        "rarity_id": 2,
        "count": 20,
        "list": ["original", "rare", "super_rare"],
    },
}
