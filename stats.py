def word_count(text):
    text_list = text.split()
    return len(text_list)

def get_books_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text
