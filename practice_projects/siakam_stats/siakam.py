import csv
import pandas as pd
import numpy as np

df = pd.read_csv("siakam_stats.csv")
df_siakam = pd.DataFrame(df)
print(df_siakam.head())
