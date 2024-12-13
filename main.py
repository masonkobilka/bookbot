

def main():
    test_book = "./books/frankenstein.txt"
    text_report(test_book)


def get_text(file_location):
    with open(file_location) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Create dictionary for values
    c_dict = {}
    for character in characters:
        c_dict[character] = 0
    
    text = text.lower()
    for i in c_dict:
        for c in text:
            if (i == c):
                c_dict[i] += 1
    
    return c_dict


def text_report(text_location):
    # collect data
    text = get_text(text_location)
    word_count = count_words(text)
    characters_count = count_characters(text)
    # Get max digit count
    max_digits = 0
    for c in characters_count:
        string = str(characters_count[c])
        if len(string) > max_digits:
            max_digits = len(string)
    
     # print data
    print(f"--- Begin report of '{text_location}' ---")
    print(f"Word count: {word_count}\n")
    for c in characters_count:
        num_digits = len(str(characters_count[c]))
        if num_digits < max_digits:
            extra_space = ' ' * (max_digits - num_digits)
            print(f"'{c}' used {characters_count[c]}{extra_space} times")
        else:
            print(f"'{c}' used {characters_count[c]} times")
    print("--- End Report ---")
    


main()