import sys
from stats import get_num_words, get_num_characters, sorted_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    num_words = get_num_words(get_book_text(sys.argv[1]))
    num_characters = get_num_characters(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {sys.argv[1]}...")
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