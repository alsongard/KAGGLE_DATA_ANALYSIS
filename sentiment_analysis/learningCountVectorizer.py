from sklearn.feature_extraction.text import CountVectorizer
mySentence = ["john likes ice cream", "john hates chocolate"]

vectorizer = CountVectorizer()
vectorizer.fit(mySentence)
print(vectorizer.vocabulary_)


print(vectorizer.transform(mySentence).toarray())
