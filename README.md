# Project description and instruction for launching

## Description
This project merges two sources about NFTs: [Open Sea](https://opensea.io), another from [NFT Showroom](https://nftshowroom.com). It brings more labels regarding NFTs and broader variency of e-currencies, which may be used by data science teams, for example, to analyse determinant factors of price.

Source of a ready CSV file from NFT Showroom can be found [here](https://www.kaggle.com/datasets/vepnar/nft-art-dataset).

## Instruction
First, copy paste following lines to your terminal shell, depending on you operating system.

### MacOS
```
python -m pip3 install requests
python -m pip3 install fastparquet
python -m pip3 install -q findspark
python -m pip3 install pyspark
pyspark --num-executors 2

brew install --cask homebrew/cask-versions/temurin8
brew install --cask android-sdk
```
