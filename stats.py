def get_num_words(file_contents):
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
    return len(file_contents_list_2)

def get_num_characters(file_contents):
    file_contents_list = file_contents.splitlines()
    file_contents_list_1 = []
    file_contents_list_2 = []
    file_contents_list_3 = []
    file_contents_dict_1 = {}
    for i in range(0, len(file_contents_list)):
        a = []
        a = file_contents_list[i].split(" ")
        for j in range(len(a)):
            file_contents_list_1.append(a[j])
    for i in range(len(file_contents_list_1)):
        file_contents_list_2.append(file_contents_list_1[i])
    for i in range(len(file_contents_list_2)):
        b = file_contents_list_2[i]
        for j in range(len(b)):
            if b[j] is not None:
                file_contents_list_3.append(b[j])
    for key in file_contents_list_3:
        lowered = key.lower()
        if lowered in file_contents_dict_1:
            file_contents_dict_1[lowered] += 1
        else:
            file_contents_dict_1[lowered] = 1
    return file_contents_dict_1

def sort_on(pair_dict):
    return pair_dict["num"]

def sorted_dict(num_characters):
    character_list = []
    for ch in num_characters:
        character_list.append({"char": ch, "num": num_characters[ch]})
    # print(character_list.sort(reverse=True, key=sort_on))
    character_list.sort(reverse=True, key=sort_on)
    return character_list