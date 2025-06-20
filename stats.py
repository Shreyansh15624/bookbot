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