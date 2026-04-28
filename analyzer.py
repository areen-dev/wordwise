def count_words(text):
    """function which takes string and splits it and count the appearnece of each word"""
    word_list = text.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


def search_word(word_dict, word):
    """function which searches for a word in word_dict dictionary"""
    if word in word_dict:
        return f"{word} found --- {word_dict[word]} times"
    else:
        return f"{word} not found"


def find_missing_words(word_dict, target_words):
    """function which shows which words are missing in the word_dict dictionary"""
    missing_words_list = []
    for words in target_words:
        if words not in word_dict:
            missing_words_list.append(words)

    return missing_words_list
