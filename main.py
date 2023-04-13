# Поварская книга
file = 'recipes.txt'


# читаем файл и получаем словарь
def read_recipes():
    with open('recipes.txt', 'rt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            ingredients = []
            ingredients_count = f.readline()
            for count in range(int(ingredients_count)):
                ing = f.readline()
                ingredient, quantity, m = ing.strip().split('|')
                ingredients.append({'ingredient': ingredient, 'quantity': int(quantity), 'm': m})
                res = {dish_name: ingredients}
            d = f.readline()
            cook_book.update(res)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingrid in cook_book[dish]:
                if ingrid['ingredient'] in shopping_list:
                    shopping_list[ingrid['ingredient']]['quantity'] += ingrid['quantity'] * person_count
                else:
                    shopping_list[ingrid['ingredient']] = {'m': ingrid['m'],
                                                           'quantity': (ingrid['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return shopping_list


person_count = 3
dishes = ['Омлет', 'Фахитос', 'Маленький мальчик', 'Запеченный картофель']
cook_book = read_recipes()
print(read_recipes())
print()
print(get_shop_list_by_dishes(dishes, person_count, cook_book))
