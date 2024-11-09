#4. Создайте словарь со списком вещей 
#для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную 
#грузоподъёмность. Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

# Создайте словарь со списком вещей для похода в качестве ключа и их 
# массой в качестве значения. Определите какие вещи влезут в рюкзак передав 
# его максимальную грузоподъёмность.

camping_kit = {"Фонарик": 1, "Котелок": 1, "Вода": 10, "Еда": 13, "Салфетки": 1, "Спальник":2}
list_inventory = []
size = int(input("Введите вес рюкзака в кг.: "))
remained = []

for key, value in camping_kit.items():
    if value <= size:
        size -= value
        list_inventory.append(key)

if len(camping_kit) > len(list_inventory):
    for invent in camping_kit:
        if invent not in list_inventory:
            remained.append(invent)
    print(f"Поместилось {list_inventory}, не поместилось {remained}")
else:
    print(f"Постилось {list_inventory}, ничего не осталось")