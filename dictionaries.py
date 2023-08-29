import re

def word_frequency(sentence):
    words = re.findall(r'\w+', sentence.lower())
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict
