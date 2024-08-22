import pandas as pd

data_df = pd.read_csv("./data/imdb_labelled.txt", names=["sentence", "label"], sep="\t", on_bad_lines="skip")
print(data_df)
data_df["source"] = "imdb"
print(data_df)

#clean data
print(data_df.isnull().sum())

#value counts for checking number of times value appear
print(data_df["label"].value_counts())