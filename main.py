def get_books_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    print(get_books_text("./books/frankenstein.txt"))

if __name__ == "__main__":
    main()
