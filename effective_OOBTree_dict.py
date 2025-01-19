import csv
from timeit import timeit
from BTrees.OOBTree import OOBTree

# Функція для завантаження даних із CSV файлу
def load_data(filename):
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['ID'] = int(row['ID'])  # Перетворюємо ID у ціле число
            row['Price'] = float(row['Price'])  # Конвертуємо ціну у float
            data.append(row)
    return data

# Додавання товарів у OOBTree
def add_item_to_tree(tree, item):
    tree[item['ID']] = {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': item['Price']
    }

# Додавання товарів у словник
def add_item_to_dict(dictionary, item):
    dictionary[item['ID']] = {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': item['Price']
    }

# Діапазонний запит для OOBTree
def range_query_tree(tree, min_price, max_price):
    return list(tree.items(min_price, max_price))

# Діапазонний запит для словника
def range_query_dict(dictionary, min_price, max_price):
    return [
        (key, value)
        for key, value in dictionary.items()
        if min_price <= value['Price'] <= max_price
    ]

# Основна функція
def main():
    # Завантаження даних із файлу
    filename = "generated_items_data.csv"
    data = load_data(filename)

    # Ініціалізація структур даних
    tree = OOBTree()
    dictionary = {}

    # Додавання даних у структури
    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    # Параметри для діапазонного запиту
    min_price, max_price = 50.0, 150.0

    # Вимірювання продуктивності для OOBTree
    tree_time = timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)

    # Вимірювання продуктивності для словника
    dict_time = timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)

    # Вивід результатів
    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main()