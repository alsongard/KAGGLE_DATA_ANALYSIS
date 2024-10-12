import pandas as pd
import matplotlib.pyplot as plt

column_names = ["id", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
data_df = pd.read_csv("./data/newsCorpora.csv", header=None, delimiter="\t", index_col=False, names=column_names)

## check if data is clean
print(data_df.isna().sum()) # publisher 2 empyty values

data_df = data_df.dropna(axis=0)

print(data_df.isna().sum()) # got none

print(data_df)

# get info on columns
print(data_df.info())



#  to 
# convert to datetime object
data_df["TIMESTAMP"] = pd.to_datetime(data_df["TIMESTAMP"])
print(data_df.dtypes)
data_df["MONTHS"] = data_df["TIMESTAMP"].apply(lambda date: date.month)
print(data_df)

# check  
# print(data_df["TIMESTAMP"].head(40))


# assign new column of year and month
# data_df["year"] = data_df["TIMESTAMP"].dt.year
# data_df["month"] = data_df["TIMESTAMP"].dt.month

# print(data_df["year"].value_counts())
# print(data_df["month"].value_counts())


# EDA : Exploratory Data Analysis
# check category values
print(data_df["CATEGORY"].value_counts())

category_counts = data_df["CATEGORY"].value_counts()
print(category_counts.index)
print(category_counts.values)

index_values = {
    "b": "Business",
    "e": "Entertainment",
    "t": "Technology",
    "m": "Medical"
}
category_counts.index = category_counts.index.map(index_values)
# explodes = (0.02, 0.02, 0.02, 0.02)
# print(category_counts)
# category_counts.plot(kind="pie", autopct="%1.1f%%", explode=explodes, startangle=90)
# plt.title("Categories")
# plt.show()
legend_titles = category_counts.index
plt.figure(figsize=(10,6))
# figsize=(width, height)
bar_labels = ['red', 'blue', 'black', 'orange']
category_counts.plot(kind='barh', color=bar_labels, width=0.4)
plt.show()


