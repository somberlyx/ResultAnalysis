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

#Gender Ditribution
# plt.figure(figsize=(5,5))
# ax = sns.countplot(data = df, x = 'Gender')
# ax.bar_label(ax.containers[0])
# plt.show()

#Effect of ParentEducation on student scores
# gb = df.groupby("ParentEduc").agg({"MathScore":'mean', "ReadingScore": 'mean', "WritingScore":'mean'})
# print(gb)

# plt.figure(figsize=(4,4))
# sns.heatmap(gb, annot=True)
# plt.title("Relationship between Parent's Education and Students' scores")
# plt.show()

# gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean', "ReadingScore": 'mean', "WritingScore":'mean'})
# print(gb1)

# plt.figure(figsize=(4,4))
# sns.heatmap(gb1, annot=True)
# plt.title("Relationship between Parent's Marital Status and Students' scores")
# plt.show()

#box plot of each student scores

sns.boxenplot(data = df, x = 'MathScore')
plt.show()

sns.boxenplot(data = df, x = 'ReadingScore')
plt.show()

sns.boxenplot(data = df, x = 'WritingScore')
plt.show()

