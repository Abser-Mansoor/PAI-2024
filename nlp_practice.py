import numpy as np
import abc as ab
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import nltk as nlp
import re as regex
import sklearn as sk

nlp.download('punkt_tab')
nlp.download('wordnet')
nlp.download('stopwords')

print(nlp.tokenize.word_tokenize('Hello This is a test of the automatic pager system. Do not be alarmed. This is a test'))
print(nlp.tokenize.sent_tokenize('Hello This is a test of the automatic pager system. Do not be alarmed. This is a test'))
words = ['he', 'am' ,'not' ,'jumping', 'nor', 'is', 'he' ,'running','.', 'he', 'is', 'walking', 'just', 'as', 'someone', 'walks']
print([nlp.PorterStemmer().stem(word) for word in words])
print([nlp.WordNetLemmatizer().lemmatize(word) for word in words])
print([nlp.WordNetLemmatizer().lemmatize(word,pos='v') for word in words])
print([word for word in words if word.lower() not in set(nlp.corpus.stopwords.words('english'))])
paragraph = """This is an example of a paragraph string in Python.
It can span multiple lines, and you can include as much text as you want.
Using triple quotes is a convenient way to define multi-line strings."""
sentences = nlp.tokenize.sent_tokenize(paragraph)
print("\n")
for sentence in sentences :
    words = nlp.tokenize.word_tokenize(sentence)
    print(f"{[nlp.PorterStemmer().stem(word) for word in words]}")

print("\n")
for sentence in sentences :
    words = nlp.tokenize.word_tokenize(sentence)
    print(f"{[nlp.WordNetLemmatizer().lemmatize(word) for word in words if word not in set(nlp.corpus.stopwords.words('english'))]}")

corpus = []

for sentence in sentences :
    review = regex.sub('[^a-zA-Z]',' ',sentence)
    review = review.lower().split()
    review = [nlp.WordNetLemmatizer().lemmatize(word) for word in review if word not in set(nlp.corpus.stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
print('\n')
x = sk.feature_extraction.text.CountVectorizer(max_features=1500).fit_transform(corpus).toarray()
print(x)
print(f"\n{sk.feature_extraction.text.TfidfVectorizer().fit_transform(corpus).toarray()}")

vec1 = np.array([3,7,3])
vec2 = np.array([1,9,4])

print(f"\nCosine Similarity: {np.round(np.dot(vec1,vec2)/np.linalg.norm(vec1)*np.linalg.norm(vec2),2)}")

description = """Python is a versatile programming language that is widely used in various fields, such as web development, data science, artificial intelligence, and more.
Its simple syntax and readability make it an excellent choice for beginners and experienced developers alike.
With a rich ecosystem of libraries and frameworks, Python allows developers to build complex applications with ease."""

text = regex.sub('\[[0-9]*\]',' ',description)
text = regex.sub('\s+',' ', text)
text = text.lower()
text = regex.sub('\d',' ',text)
text = regex.sub('\s+',' ',text)

desc_sents = nlp.tokenize.sent_tokenize(description)
for sentence in desc_sents :
    sentence = [word for word in sentence if word not in set(nlp.corpus.stopwords.words('english'))]

#model = gs.models.Word2Vec(desc_sents,min_count=1)

#print(model.wv('python'))
#print(model.wv.most_similar('syntax'))

