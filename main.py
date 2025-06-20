from stats import get_num_words, get_num_characters, sorted_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
        
def main_1():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    num_characters = get_num_characters(get_book_text("books/frankenstein.txt"))
    for key in num_characters:
        print(f"'{key}': {num_characters[key]}")

def main():
    path = "books/frankenstein.txt"
    num_words = get_num_words(get_book_text(path))
    num_characters = get_num_characters(get_book_text(path))
    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_list = sorted_dict(num_characters)
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()