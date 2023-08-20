# Задание №1
#
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


# Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for i in cook_book[dish]:
                if i['ingredient_name'] not in res:
                    res[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
                else:
                    res_2 = res[i['ingredient_name']]
                    res[i['ingredient_name']] = {'measure': i['measure'], 'quantity': res_2['quantity'] + int(i['quantity']) * person_count}

        else:
            return f'Блюдо "{dish}" отсутствует в кулинарной книге!'
    return res

print(get_shop_list_by_dishes(['Омлет','Фахитос'], 2))

