import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("iguoadala.csv")
df_iguoadala = pd.DataFrame(df)
print(df_iguoadala.head())