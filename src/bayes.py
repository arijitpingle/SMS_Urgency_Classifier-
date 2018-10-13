# bayes.py
# naive bayes method

URGENCIES = {
    "NOT_URGENT": 1,
    "SLIGHTLY_URGENT": 2,
    "URGENT": 3,
    "VERY_URGENT": 4
}

class Bayes():
    word_bank = {}
    messages = []
    def __init__(self, messages):
        self.messages = messages

        for message in self.messages:
            split = message["message"].split()

            for word in split:
                self.word_bank[word] = [0.0, 0.0, 0.0, 0.0, 0.0]

    def train(self):
        for message in self.messages:
            split = message["message"].split()

            for word in split:
                self.word_bank[word][0] += 1 

                urgency = message["urgency"]
                index = URGENCIES[urgency]
                self.word_bank[word][index] += 1

