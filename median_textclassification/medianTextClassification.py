import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

column_names = ["id", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
data_df = pd.read_csv("./data/newsCorpora.csv", header=None, delimiter="\t", index_col=False, names=column_names)

## check if data is clean
print(data_df.isna().sum()) # publisher 2 empyty values

data_df = data_df.dropna(axis=0)

print(data_df.isna().sum()) # got none

print(data_df)
data_df = data_df.drop(columns="id")


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
print(f"The shape of data_df is {data_df.shape}")


# MODEL CREATING

# get feature and target
x_feature = data_df["TITLE"]
y_target = data_df["CATEGORY"]
# split data
x_sentence_train, x_sentence_test, y_train, y_test = train_test_split(x_feature, y_target, test_size=0.33, random_state=1000)
print(x_sentence_train)
print("\n")
print(x_sentence_test)
print("\n")
print(y_train)
print("\n")
print(y_test)


## convert our text into numerical representation
## using Term-Frequency -Inverse-Document-Frequency

vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
mySentences_train_vector = vectorizer.fit_transform(x_sentence_train)


NB = MultinomialNB(alpha=0.5)
NB.fit(mySentences_train_vector,y_train)