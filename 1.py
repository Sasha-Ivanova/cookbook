# Задание №3

import os
def custom_key(len_text):
    return len_text[1]

path = 'Задание_3'
directory = os.listdir(path)
file_list = []
id = 0
for file in directory:
    with open(os.path.join(path, file), encoding='utf-8') as f:
        text = f.readlines()
        file_list.append([directory[id], len(text),text])
        id +=1
sort = file_list.sort(key=custom_key)

with open('result.txt', 'w', encoding='utf-8') as result_file:
    result_file.write(file_list[0][0] + '\n' + str(file_list[0][1]) + '\n' + (" ".join(file_list[0][2])) + '\n')
    result_file.write(file_list[1][0] + '\n' + str(file_list[1][1]) + '\n' + (" ".join(file_list[1][2])) + '\n')
    result_file.write(file_list[2][0] + '\n' + str(file_list[2][1]) + '\n' + (" ".join(file_list[2][2])) + '\n')

