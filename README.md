# Project description and instruction for launching

## Description
This project merges two sources about NFTs: [Open Sea](https://opensea.io), another from [NFT Showroom](https://nftshowroom.com). It brings more labels regarding NFTs and broader variency of e-currencies, which may be used by data science teams, for example, to analyse determinant factors of NFT price.

Source of a ready CSV file from NFT Showroom can be found [here](https://www.kaggle.com/datasets/vepnar/nft-art-dataset).

## Instruction
This is a guide on how to run the project using local server. Copy-paste following lines **line by line** to your terminal, depending on your operating system. If the third step runs with an error, try moving on with the rest of commands, as you might have all the needed packages installed.

#### MacOS
```
git clone https://github.com/marfappv/data_eng_group
cd data_eng_group/environments
bash MacOs_env.sh
cd ..
python3 full_MacOS_script.py
```

#### Linux
```
git clone https://github.com/marfappv/data_eng_group
cd data_eng_group/environments
bash Linux_env.sh
cd ..
python3 full_MacOS_script.py
```

#### Check the imputed RDS

1. Type the following line to your teminal:
```
psql --host=nfts.cuweglfckgza.eu-west-2.rds.amazonaws.com --port=5432 --username=marfapopova21 --password --dbname=nfts
```
2. Insert password: qwerty123. Hit enter.
3. Type the following 3 lines in terminal:
```
\dn
\dt nfts.*
select * from nfts.assets;
```