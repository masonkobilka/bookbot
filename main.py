def word_count(text):
    text_list = text.split()
    return len(text_list)

def get_books_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text_length = word_count(get_books_text("./books/frankenstein.txt"))
    print(f"{text_length} words found in the document")

if __name__ == "__main__":
    main()
