from stats import get_num_words, get_num_characters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
        
def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    num_characters = get_num_characters(get_book_text("books/frankenstein.txt"))
    for key in num_characters:
        print(f"'{key}': {num_characters[key]}")
        
main()