## CountVectorizer
How CountVectorizer works:
The count vectorizer has  4 steps namely:
- Tokenization
- Vocabulary
- Feature Vector
```
"I love Programming", "Programming in Python", "I love python"
```
Given the following string 
1. **Defining a baseline model:**


2. **spliting the data set:**

*overfitting:*


## DATA FEATURES:
**labels:**
0 = stands for a negative review from the user
1 = stands for a positive review from a user
### advancement of deep neural networks and how it can be applied in text
sentiment analysis is the process of analysing text to get valuable information.
Used in text classification
Used in Natural Language Processing.(NLP)
Text classification is used in the detectionof spams, auto tagging of customer queries, and categorization of text into defined topics.


bag of words (BOM) model, this is a common way of NLP to create vectors out of text
Remember that the vocabulary contains a words from the given sentences(is a list) and takes unique words. 
Example:
In the given below sentences "John" would appear once even though it appears in each of the sentence:
```
mySentence = ["John likes ice cream", "John hates chocolate"]
```

**Check vocabulary for given sentences use:**
```
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorizer.fit(mySentence)
print(vectorizer.vocabulary_)
```
Result : ``{'john': 4, 'likes': 5, 'ice': 3, 'cream': 1, 'hates': 2, 'chocolate': 0}``

to generate feature vector
``print(vectorizer.transform(mySentence).toarray())``
