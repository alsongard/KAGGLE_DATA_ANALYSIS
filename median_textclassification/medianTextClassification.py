import pandas as pd

column_names = ["id", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
data_df = pd.read_csv("./data/newsCorpora.csv", header=None, delimiter="\t", index_col=False, names=column_names)

## check if data is clean
print(data_df.isna().sum()) # publisher 2 empyty values

data_df = data_df.dropna(axis=0)

print(data_df.isna().sum()) # got none

print(data_df)

# get info on columns
print(data_df.info())

# check category values
print(data_df["CATEGORY"].value_counts())

#  to 
# convert to datetime object
data_df["TIMESTAMP"] = pd.to_datetime(data_df["TIMESTAMP"])
print(data_df.dtypes)
data_df["MONTHS"] = data_df["TIMESTAMP"].apply(lambda date: date.month)
print(data_df)

# check  
print(data_df["TIMESTAMP"].head(40))
