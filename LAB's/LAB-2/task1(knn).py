from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import metrics
import pandas as pd
from sklearn.model_selection import KFold,train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
import re
from sklearn.neighbors import KNeighborsClassifier
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

playstoredata = pd.read_csv('googleplaystore_user_reviews.csv')

#Finding the Missing Values
print(format(playstoredata.isnull().sum()))
df = pd.concat([playstoredata.Translated_Review, playstoredata.Sentiment], axis = 1)

#Eliminating NAN values
df.dropna(axis = 0, inplace= True)
#Performing Lable Encoding
label_encoder = preprocessing.LabelEncoder()
df['Sentiment'] = label_encoder.fit_transform(df['Sentiment'])

text_list = []
for i in df.Translated_Review :
    review = re.sub('[^a-zA-Z]', ' ', i)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    text_list.append(review)


cv = CountVectorizer(max_features = 1000)
x = cv.fit_transform(text_list).toarray()
y = df.iloc[:, 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

#creating Gaussin Naive Bayes object for classification
classifer = KNeighborsClassifier(n_neighbors=3)
#Training Model
classifer.fit(x_train,y_train)
#predicting Output
y_predict = classifer.predict(x_test)
cm = confusion_matrix
#printing confusion matrix
print(cm)
accuracy = accuracy_score(y_test,y_predict)
print(accuracy)