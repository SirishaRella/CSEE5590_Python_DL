from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
import numpy as np

model = load_model('saved_model.h5')
test_data = ["A lot of good things are happening. We are respected again throughout the world, and that's a great thing"]
max_features = 200
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(test_data)
X = tokenizer.texts_to_sequences(test_data)
max_len = 28
X = pad_sequences(X, maxlen=max_len)
class_names = ['positive', 'negative']
preds = model.predict(X)
print(preds)
classes = model.predict_classes(X)
print(classes)
print(class_names[classes[0]])

