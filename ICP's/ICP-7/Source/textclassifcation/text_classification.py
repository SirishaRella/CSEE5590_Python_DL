from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from nltk.corpus import stopwords
import nltk

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

tfidf_Vect = TfidfVectorizer(ngram_range=(3,4))
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

#setting stopwords
nltk.download('stopwords')
set(stopwords.words('english'))

# print(tfidf_Vect.vocabulary_)
neigh = KNeighborsClassifier(n_neighbors=1)
#neigh = MultinomialNB()
neigh.fit(X_train_tfidf, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)


predicted = neigh.predict(X_test_tfidf)

score = metrics.accuracy_score(twenty_test.target, predicted)
print(score)