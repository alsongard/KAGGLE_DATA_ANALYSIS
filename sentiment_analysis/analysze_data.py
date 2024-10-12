import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

data_df = pd.read_csv("./data/imdb_labelled.txt", names=["sentence", "label"], sep="\t", on_bad_lines="skip")
print(data_df)
data_df["source"] = "imdb"
print(data_df)

print("\n")


print("The attributes or columns and data types of the data are: ")
print(data_df.info())
print("\n")

#clean data
print(data_df.isnull().sum())

#value counts for checking number of times value appear
print(data_df["label"].value_counts())  # 385 values = 1 (positive) and 362 values = 0(negative)
print("\n")

# split the data
# takes all labels and convert the label data into a numpy array
y = data_df["label"].values  # values are our target
print(f"Type of y is : {type(y)}")
print("convert the sentence data into a numpy array")
print(f"the type of sentence is {type(y)} and the length is {y.size}")
print(y)
print("\n")

#take all sentences
sentence = data_df["sentence"].values
#convert the sentence data into a numpy array 
print("convert the sentence data into a numpy array")
print(f"the type of sentence is {type(sentence)} and the length is {sentence.size}")
print(sentence[0:20])
print("\n")


#split
sentence_train, sentence_test, y_train, y_test = train_test_split(sentence, y, test_size=0.25, random_state=1000)
print("After the data has been splitted check length and data itself : ")
print(f"The length of the sentence_train is {sentence_train.size}")
print(f"Data is :  \n {sentence_train[0:20]}")
print("\n")

# generate vocabulary for the given sentences
# generating a feature vector for each sentence : shows the number of appearance of the words in the vocabulary for each 
# sentence a non-zero value represent that the word is present (vice versa)
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(sentence_train)

# check vocabulary
# print(f"vocabulary based on training data set : X_train is {vectorizer.vocabulary_}")
X_test = vectorizer.fit_transform(sentence_test)

print("Feature vector of X_train is : ")
print(X_train.toarray())
print(len(X_train.toarray())) # 560 echo $((0.75 * 746)) = 559.5

# check the vocabulary (unique words in the sentences given)
print("\n")
print("The vocabulary used is : ")
print(vectorizer.get_feature_names_out())
print(f"the type of type(vectorizer.get_feature_names_out()) is {type(vectorizer.get_feature_names_out())}")
#get the lenght of the array
vocabulary = vectorizer.get_feature_names_out()
print(f"The lenght of vectorizer.get_feature_names_out is {vocabulary.size}")

# classification
# use the logistic regresion 
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
# about converting data to numerical datatype
score = classifier.score(X_test, y_test)

print(f"Accuracy of the model is classifying X_test data is {score}")