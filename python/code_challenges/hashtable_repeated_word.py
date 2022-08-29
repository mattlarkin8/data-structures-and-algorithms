from data_structures.hashtable import Hashtable
import re


def first_repeated_word(text):
    word_list = text.split()
    words_seen = []
    for candidate in word_list:
        word = re.sub(r'[^A-Za-z]+','', candidate.lower())
        if word in words_seen:
            return word
        words_seen.append(word)

    return None
