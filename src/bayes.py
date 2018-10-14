# bayes.py
# naive bayes method

from math import log
import re

URGENCIES = {
    "NOT_URGENT": 0,
    "SLIGHTLY_URGENT": 1,
    "URGENT": 2,
    "VERY_URGENT": 3
}


class Bayes():
    word_bank = {}
    messages = []
    total_words = 0
    class_totals = [0.0, 0.0, 0.0, 0.0]
    def __init__(self, messages):
        self.messages = messages

        bal = [1.0, 1.0, 1.0, 1.0, 1.0]

        
        for message in self.messages:
            if "?" in message:
                self.word_bank['?'] = [1.0, 1.0, 1.0, 1.0, 1.0]

            if "!!!" in message:
                self.word_bank['!!!'] = [1.0, 1.0, 1.0, 1.0, 1.0]
            elif "!!" in message:
                self.word_bank['!!'] = [1.0, 1.0, 1.0, 1.0, 1.0]
            elif "!" in message:
                self.word_bank['!'] = [1.0, 1.0, 1.0, 1.0, 1.0]

            split = message["message"].lower().split()


            for word in split:
                self.word_bank[word] = [1.0, 1.0, 1.0, 1.0, 1.0]
    
    def __str__(self):
        return "Totals: {}\n{}".format(self.class_totals, 
                self.word_bank.__str__())
    

    def train(self):
        for message in self.messages:
            urgency = message['urgency']
            index = URGENCIES[urgency]

            if "?" in message:
                self.word_bank['?'][0] += 1
                self.word_bank['?'][index + 1] += 1

            if "!!!" in message:
                self.word_bank['!!!'][0] += 1
                self.word_bank['!!!'][index + 1] += 1

            elif "!!" in message:
                self.word_bank['!!!'][0] += 1
                self.word_bank['!!!'][index + 1] += 1

            elif "!" in message:
                self.word_bank['!!!'][0] += 1
                self.word_bank['!!!'][index + 1] += 1

            split = message["message"].split()

            for word in split:
                word = word.lower()
                self.word_bank[word][0] += 1

                self.word_bank[word][index + 1] += 1

                self.class_totals[index] += 1

    def gen_feature_vector(self, words):
        fv = {}
        for word in self.word_bank:
            word = word.lower()
            fv[word] = False
            if word in words:
                fv[word] = True        
        return fv

    def prob_class(self, feature_vector, clazz):
        total = 0
        index = URGENCIES[clazz]
        for f in feature_vector.keys():
            
            p = 0
            y = self.class_totals[index]
            w = self.word_bank[f][index + 1]

            if feature_vector[f]:
                p = w / y 
            else:
                p = (y - w) / y

            total += log(p)
    

        return total + log( y / sum(self.class_totals) )

    def classify(self, feature_vector):
        best_class = 'NOT_URGENT'
        best_prob = 0
        for clazz in URGENCIES.keys():
            prob = self.prob_class(feature_vector, clazz)
            if prob < best_prob:
                best_prob = prob
                best_class = clazz

        return best_class
