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
