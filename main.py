from pprint import pprint

from tasks import get_cook_book, get_shop_list_by_dishes, combining_files

if __name__ == "__main__":
    pprint(get_cook_book())
    pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))
    combining_files()
