def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_no_of_words(file_contents):
    file_contents_list = file_contents.splitlines()
    file_contents_list_1 = []
    file_contents_list_2 = []
    for i in range(0, len(file_contents_list)):
        a = []
        a = file_contents_list[i].split(" ")
        for j in range(len(a)):
            file_contents_list_1.append(a[j])
    for i in range(len(file_contents_list_1)):
        if file_contents_list_1[i] not in {' ', '', '\n', None}:
            file_contents_list_2.append(file_contents_list_1[i])
    
    for i in range(len(file_contents_list_2)):
        print(f"{file_contents_list_2[i]} & {type(file_contents_list_2[i])}")
    
    return len(file_contents_list_2)
        
def main():
    num_words = get_no_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    
main()