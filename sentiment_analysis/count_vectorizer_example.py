from sklearn.feature_extraction.text import CountVectorizer

senteces = [
    "I love programming",
    "programming in python is fun",
    "I love python"
]

## initialize vectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(senteces)

print(X.toarray())

print(vectorizer.get_feature_names_out())


new_sentences = [
    "John likes ice creams",
    "John hates chocolate"
]
Y = vectorizer.fit_transform(new_sentences)

print(Y.toarray())
print(vectorizer.get_feature_names_out())