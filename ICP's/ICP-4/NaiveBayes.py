from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn import preprocessing
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np

#Loading the data_set
iris_data = pd.read_csv('iris.csv')

#Label encoding the values
label_encoder = preprocessing.LabelEncoder()
data = iris_data
iris_data = label_encoder.fit_transform(iris_data.values[:, 4])

#preparing dataset
X = data.values[:, :4]
Y = iris_data

#Naive Bayes Algorithm
model = GaussianNB()
kf = KFold(n_splits=10, shuffle=True,random_state=50)
accuracy = []

for train_index, test_index in kf.split(X):
   X_train, X_test = X[train_index], X[test_index]
   Y_train, Y_test = Y[train_index], Y[test_index]

   #Training the model
   model.fit(X_train, Y_train)

   #Predictions
   predicted = model.predict(X_test)

   #Accuracy score
   y_pred = model.predict(X_test)
   print("Accuracy score: ", metrics.accuracy_score(Y_test, y_pred))
   accuracy.append(metrics.accuracy_score(Y_test, y_pred))

   #Confusion Matrix
   confusionmatrix = confusion_matrix(Y[test_index], predicted)
   print(confusionmatrix)

#Mean Accuracy
print("Mean Accuracy Score: ", np.mean(accuracy))



