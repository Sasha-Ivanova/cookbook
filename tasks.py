import os


# Задание №1
def get_cook_book():
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        cook_book = {}
        for dish in file:
            quantity_ingredient = int(file.readline())
            ingredients = []
            for ingredient in range(quantity_ingredient):
                name, quantity, measure = file.readline().strip().split('|')
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish.strip()] = ingredients
        return cook_book


# Задание №2
def get_shop_list_by_dishes(dishes: list, person_count: int):
    res = {}
    for dish in dishes:
        if dish in get_cook_book().keys():
            for i in get_cook_book()[dish]:
                if i['ingredient_name'] not in res:
                    res[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
                else:
                    res_2 = res[i['ingredient_name']]
                    res[i['ingredient_name']] = {'measure': i['measure'],
                                                 'quantity': res_2['quantity'] + int(i['quantity']) * person_count}

        else:
            return f'Блюдо "{dish}" отсутствует в кулинарной книге!'
    return res


# Задание №3
def custom_key(len_text):
    return len_text[1]


def combining_files():
    path = 'files'
    directory = os.listdir(path)
    file_list = []
    id = 0
    for file in directory:
        with open(os.path.join(path, file), encoding='utf-8') as f:
            text = f.readlines()
            file_list.append([directory[id], len(text), text])
            id += 1
    file_list.sort(key=custom_key)
    with open('result.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(file_list[0][0] + '\n' + str(file_list[0][1]) + '\n' + (" ".join(file_list[0][2])) + '\n')
        result_file.write(file_list[1][0] + '\n' + str(file_list[1][1]) + '\n' + (" ".join(file_list[1][2])) + '\n')
        result_file.write(file_list[2][0] + '\n' + str(file_list[2][1]) + '\n' + (" ".join(file_list[2][2])) + '\n')
        print('Файлы объединены!')
