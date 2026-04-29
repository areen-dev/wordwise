from analyzer import count_words, find_missing_words, search_word
from utils import clean_text, format_results


def main():
    word_dict = {}
    while True:
        print("1. Analyze text")
        print("2. Search for a word")
        print("3. Check missing words")
        print("4. Exit")

        menu_input = input("What to do: \n > ").lower()
        if menu_input in ("1", "analyze text", "one"):
            user_input1 = input("Enter text \n > ")
            clean_text1 = clean_text(user_input1)
            word_dict = count_words(clean_text1)
            for key, value in word_dict.items():
                print(format_results(key, value))
        elif menu_input in ("2", "search for a word", "two"):
            user_input2 = input("Search word \n > ")
            clean_text2 = clean_text(user_input2)
            found_word = search_word(word_dict, clean_text2)
            print(found_word)
        elif menu_input in ("3", "check missing words", "three"):
            user_input3 = input("Enter text \n > ")
            clean_text3 = clean_text(user_input3)
            missing_word_list = clean_text3.split()
            missng_words = find_missing_words(word_dict, missing_word_list)
            print(missng_words)
        elif menu_input in ("4", "exit", "four"):
            break
        else:
            print("Please chosse a valid opton.\n")


if __name__ == "__main__":
    main()
