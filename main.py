import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("studentResults.csv")

# print(df.describe())

# print(df.info())

# print(df.isnull().sum())

#Remove Unnamed Column
df = df.drop("Unnamed: 0", axis = 1)
print(df.head())

df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct", "05-10")