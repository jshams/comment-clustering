import nltk
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import random

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

print('MOST COMMON WORDS')
print(all_words.most_common(60))
# print('how many occurances of stupid are in the corpus')
# print(all_words["funny"])
# # This will tell us 
word_features = list(all_words.keys())[:30]
# print(sorted([(key, val) for key, val in all_words.items()], reverse=True ,key=lambda item:item[1]))
# join them by #_#, split them by "." then split the subsenences by #_# and join them by ' '
all_sentences = [' '.join(sentence.split('#_#')) for sentence in '#_#'.join(movie_reviews.words()).split('.')]