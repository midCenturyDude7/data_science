import csv
import pandas as pd
import numpy as np

df = pd.read_csv('harkless_stats.csv')
df_harkless = pd.DataFrame(df)
print(df_harkless.head())