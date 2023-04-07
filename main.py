# Поварская книга
# читаем файл
with open('recipes.txt', 'rt', encoding='utf-8') as f:
    res = f.readlines()
    print(res)
