import pandas as pd

showroom = pd.read_csv('showroom.csv')
showroom.to_parquet('showroom.parquet')