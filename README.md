# NFT ART GENERATOR

This is a python art generative code, which uses 'Pillow' python module to merge various layers into one.

## INSTALLATION 🛠

- Clone this repository into your working directory.
```sh
git clone https://github.com/adarsh-mamgain/NFT-art-generator.git
```

- Run the following command to install [`Pillow`](https://github.com/python-pillow/Pillow/) and other dependencies
```sh 
pip3 install -r requirements.txt
```

---
---

## WORKING 🚀

### CODE/CONFIG.PY

All the required configurations are stored and accessed from [code/config.py](https://github.com/adarsh-mamgain/NFT-art-generator/tree/develop/code/config.py) 

The count is the rarity percent for **original, rare** and **super_rare** out of your total edition_size (eg: 10000). You may change the count values for each rarity totaling perfect 100.

```js
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
```

**NOTE: You can modify the variable values in [code/config.py](https://github.com/adarsh-mamgain/NFT-art-generator/tree/develop/code/config.py)  file to get the required ouput.**

---

### CODE/LAYERS.PY

This file serves all elements and it's details in each layers inside the [input](https://github.com/adarsh-mamgain/NFT-art-generator/tree/develop/input)  folder.

**NOTE:** Please change the relative path name inside the called `get_element()` function for each element in the races -> layers -> elements -> inside the `list` key.

```js
...
...
"background": {
    "layer_id": "A",
    "elements": {
        "original": {
        "rarity_id": 0,
        "list": [
            {
                "element_id": 0,
                "name": "Bazaar",
                "location": "./input/background/original/Bazaar.png"
            },
            {
                "element_id": 1,
                "name": "Yellow",
                "location": "./input/background/original/Yellow.png"
            }
        ]
        }
    }
},
"armour": {
    "layer_id": "B",
    "elements": {
        "original": {
        "rarity_id": 0,
        "list": [
            {
            "element_id": 0,
            "name": "Blue",
            "location": "./input/armour/original/Blue.png"
            },
            {
            "element_id": 1,
            "name": "Violet",
            "location": "./input/armour/original/Violet.png"
            }
        ]
    }
}
...
...
```

---

### CODE/REGENERATE_METADATA.PY

This code regenerates the metadata inside the `build/metadata/` for all the **#.json** files and **metadata.json**.

The new attributes `DESCRIPTION`, `BASE_IMAGE_URI`  must be changed inside the [code/config.py](https://github.com/adarsh-mamgain/NFT-art-generator/tree/develop/code/config.py) 

---

### CODE/MAIN.PY

`CODE/MAIN.PY` is the main file to generate art. The code performs the following functions `clear_data`, `get_rarity`, `create_dna`, `is_dna_unique`, `save_metadata` and `create_image`.

---
---

## ABOUT

Founder: Adarsh Mamgain

Contact: [LinkedIn](https://www.linkedin.com/in/adarsh-mamgain)