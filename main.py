import stats

def main():
    text_length = stats.word_count(stats.get_books_text("./books/frankenstein.txt"))
    print(f"{text_length} words found in the document")

if __name__ == "__main__":
    main()
