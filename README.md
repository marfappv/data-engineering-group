# Project description and instruction for launching

## Description
This project merges two sources about NFTs: [Open Sea](https://opensea.io), another from [NFT Showroom](https://nftshowroom.com). It brings more labels regarding NFTs and broader variency of e-currencies, which may be used by data science teams, for example, to analyse determinant factors of price.

Source of a ready CSV file from NFT Showroom can be found [here](https://www.kaggle.com/datasets/vepnar/nft-art-dataset).

## Instruction
This is a guide on how to run the project using local server. Copy paste following lines to your terminal shell, depending on you operating system.

1. git clone https://github.com/marfappv/data_eng_group
2. Go to your local directory
3. python -m http.server 8000
4. Open your browser at http://localhost:8000

#### MacOS
```
python -m pip3 install requests
python -m pip3 install fastparquet
python -m pip3 install -q findspark
python -m pip3 install pyspark
pyspark --num-executors 2
python -m pip3 install pyarrow

brew install --cask homebrew/cask-versions/temurin8
brew install --cask android-sdk

curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg ./AWSCLIV2.pkg -target /
```