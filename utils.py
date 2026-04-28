def clean_text(text):
    """function which converts text to lowercase and return it"""
    text = text.strip().lower()
    return text


def format_results(word, count):
    """function which format the results in word : count format"""
    return f"{word}: {count} times"