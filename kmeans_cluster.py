from gensim.models import Word2Vec
import nltk
import numpy as np
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

sentences = [
    'this is the learning good deep learning book',
    'this is another book',
    'one more book',
    'train railway station',
    'time train station',
    'time railway station train',
    'this is the new post',
    'this is about more deep learning post',
    'and this is the one']

# def cluster_sentences(sentences):
tokenized_sentences = [sentance.split(' ') for sentance in sentences]

model = Word2Vec(tokenized_sentences, size=100, min_count=5)

def sentance_to_vector(sentance, model):
    vector = [0] * 100
    iteration = 0
    for word in sentance:
        try:
            if iteration == 0:
                vector = model[word]
            else:
                vector = np.add(vector, model[word])
            iteration += 1
        except:
            pass
    if iteration == 0:
        return np.array([0] * 100)
    return np.asarray(vector) / iteration

X = np.array([sentance_to_vector(sentance, model) for sentance in tokenized_sentences])
print(X)

# Use K_means clustering to split up the sentences
def find_best_n_clusters(max_n):
    intertias = []
    for i in range(1, max_n + 1):
        clf = KMeans(n_clusters=i, random_state=42)
        clf.fit(X)
        intertias.append(clf.inertia_)

    plt.plot(range(1, max_n + 1), intertias)
    plt.show()

# cluster them
clf = KMeans(n_clusters=2, random_state=42)
clf.fit(X)
labels = clf.predict(X)
for sentance, label in zip(sentences, labels):
    print(label, sentance)