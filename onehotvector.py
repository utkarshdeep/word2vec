import numpy as np
from generateTrainingData import data
from converter import convert_data


def to_one_hot(data_point_index, vocab_size):
    temp = np.zeros(vocab_size)
    temp[data_point_index] = 1
    return temp

x_train = [] # input word
y_train = [] # output word
words, word2int, vocab_size = convert_data()

for data_word in data:
    print(word2int)
    print(word2int.get(data_word[0]))
    x_train.append(to_one_hot(word2int[data_word[0].lower()], vocab_size))
    y_train.append(to_one_hot(word2int[data_word[1].lower()], vocab_size))