import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("Breas Cancer.csv")
# print(dataset)

classes = ['Benign', 'Malignant']

X = dataset.iloc[:, 2:32].values
y = dataset.iloc[:, 1].values

print(X)
print(y)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_X_1 = LabelEncoder()
y = labelencoder_X_1.fit_transform(y)
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(30, input_dim=20, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')
my_first_nn_fitted = my_first_nn.fit(X_train, y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
y_pred = my_first_nn.predict(X_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

ax= plt.subplot()
sns.heatmap(cm, annot=True, ax = ax)

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(['Benign', 'Malignant'])
ax.yaxis.set_ticklabels(['Benign', 'Malignant'])
plt.savefig('breastcancer.png')

