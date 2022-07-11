import nltk 
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

"""
Exercises:
1) Install NLTK and test the installation.

2) Install the german packages of NLTK and corpora.

3) Choose a large german (or other non-english) corpus (> 1 or 10 MB). Load it in NLTK and use it for the following exercises.

4) Calculate the lexical richness of the selected corpus.

5) Plot the character distribution of your selected corpus.

6) Plot the word distribution of the 20 most often used words of your selected corpus.

7) Remove stopwords and repeat exercise 6 (word distribution).

8) Print a wordcloud without your stopwords.

Since you may choose the corpus and stopwords, the answers of parts 3 to 8 are individual.
This is why this exercise won't be discussed in a lecture. Please hand-in your answers in a PDF file (see iLearn).
"""

# read the file  
FILE = 'deu_news_2021_30K-sentences.txt'
f = open(FILE, encoding='utf-8', mode='r')
text2 = f.read()

# create a list of words with punctuations
list_of_words = nltk.word_tokenize(text2)

# initiate a variable which contains the default german stopwords defined in NLTK Corpus 
default_stopwords = set(stopwords.words('german'))

# only words (no numbers, punctuations, etc)
def vocabs():
    vocabs = [word.lower() for word in list_of_words if word.isalpha()]
    return vocabs

# all the words without stopwords 
def vocabs_without_stopwords():
    vocabs_temp = vocabs()
    cleaned = [x for x in vocabs_temp if x not in default_stopwords]
    return cleaned 

# exercise 4 (lexical richness)
def lexical_richness():
    # filter out punctuations
    vocabs_temp = vocabs()
    print("exercise 4 (lexical richness)")
    return len(set(vocabs_temp))/len(vocabs_temp)

# exercise 5 (character distribution)
def plot_character_distribution():
    fdist = nltk.FreqDist(ch.lower() for ch in text2 if ch.isalpha())
    print("exercise 5 (character distribution)")
    fdist.plot(25)

# exercise 6 (word distribution)
def plot_word_distribution():
    vocabs_temp = vocabs()
    fdist = nltk.FreqDist(vocabs_temp)
    print("exercise 6 (word distribution)")
    fdist.plot(20)

# exercise 7 (word distribution without stopwords)
def plot_word_dsitribution_wo_stopwords():
    vocabs_temp = vocabs_without_stopwords()
    fdist = nltk.FreqDist(vocabs_temp)
    print("exercise 7 (word distribution without stopwords)")
    fdist.plot(20)


# exercise 8 (print wordcloud without stopwords)
def wordcloud():
    print("exercise 8 (print wordcloud without stopwords)")
    width = 18
    height = 18
    plt.figure(figsize=(width, height))
    #text = 'all your base are belong to us all of your base base base'
    wordcloud = WordCloud(width=1800,height=1400).generate(str(vocabs_without_stopwords()))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


