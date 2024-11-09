#2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
list_numbers = [1, 5, 9, 1, 7, 9, 5]
new_list = []

for number in list_numbers:
    if list_numbers.count(number) > 1 and number not in new_list:
        new_list.append(number)

print(new_list)