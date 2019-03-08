import requests
from bs4 import BeautifulSoup
import nltk
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk import wordpunct_tokenize, pos_tag, ne_chunk

#Downloading all depedencies of NLTK
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

#getting the web content
html_doc = requests.get('https://en.wikipedia.org/wiki/Google')

#scrapping content using BeautifulSoup
soup = BeautifulSoup(html_doc.text, 'html.parser')


paragraph = soup.find_all('p')

#Writing contents to a file.
with open('input.txt', 'a') as f:
    for item in paragraph:
        f.write(item.text)



input = open('input.txt', 'r')

with open('output.txt', 'w') as f:

    for statement in input:

        #Tokenization
        tokens = nltk.word_tokenize(statement)

        #parts of speech
        pos = nltk.pos_tag(tokens)
        f.write("Parts of Speech: \n")
        f.write(str(pos))
        print(pos)

        #Stemming
        stemmer = PorterStemmer()
        f.write("Stemming: \n")
        for token in tokens:
            stemming = stemmer.stem(token)
            f.write(str(stemming))
            print(stemming)

        #Lemmatizaiton
        lemmatizer = WordNetLemmatizer()
        f.write("Lemmatization: \n")
        for token in tokens:
            lemmatization = lemmatizer.lemmatize(token)
            f.write(str(lemmatization))
            print(lemmatization)

        #Named Entity Recognition
        ner = ne_chunk(pos_tag(wordpunct_tokenize(statement)))
        f.write("Named Entity Recognition: \n")
        f.write(str(ner))
        print(ner)

        #Trigrams
        f.write("Trigrams: \n")
        trigrams = nltk.trigrams(statement.split())
        for item in trigrams:
            f.write(str(item))
            print(item)


