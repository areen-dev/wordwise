def count_words(text):
    """function which takes string and splits it and count the appearnece of each word"""
    word_list = text.split()
    word_dict = {}
    for word in word_list:
        count = word_list.count(word)
        word_dict.setdefault(word, count)
    return word_dict
