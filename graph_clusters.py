from nltk.corpus import wordnet

class ClusterComments():
    def __init__(self, sentances=None):
        self.sentances = sentances
    
    def get_hist_words(self):
        '''will put all the words into a histogram and return the hist'''
        word_hist = {}
        for word in self.generate_words():
            if word in word_hist:
                word_hist[word] += 1
            else:
                word_hist[word] = 1


    def clean(self, word):
        '''cleans a word by only yielding the word without punctuation'''
        clean_word = ''
        for letter in word:
            if letter.isalpha():
                clean_word += letter.lower()
        return clean_word

    def generate_words(self):
        '''iterates through self.sentaces (list) and generates all words'''
        for sentance in self.sentances:
            for word in sentance:
                yield self.clean(word)

    def create_thesaurus_graph(self):
        '''Turn the thesaurus into graph. not a digraph'''
        pass

    def create_thesaurusized_hist(self, word_hist):
        '''iterate through the word hist in order of popularity
        add each word to a new histogram and add its occurances
        [not occurances rather an object that contains that word
        and all words related to it. and all of their counts]
        as you add the words, check if the word has a path to any
        word that is already in the hist. This can be done via a
        BFS from that word and see if any of its neighbors are in
        the dict from the node's is_is_dict property.
        It should also skip over any conjunction words, determiners,
        or prepositions'''
        pass

    def get_categories(self):
        '''from the thesarasized hist, get the top 3 categories.'''
        pass

    def categorize_sentace(self):
        '''given a single sentance determine what category it belongs to'''
        pass

    def categorize_sentances(self):
        '''iterate throgh each sentance and determine their category.
        remember: when searching ensure the sentance is clean
        add them to an array associated with that cat'''
        pass

    def _create(self):
        ''''''
        # word_hist = self.get_hist_words()
        # thesaurus_graph = self.create_thesaurus_graph()
        # thesaurus_hist = self.create_thesaurusized_hist(word_hist)
        pass
