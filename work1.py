#         Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#                  Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки


def fill_array(a1, d, n):
    my_list = []
    for i in range(n):
        my_list.append(a1 + (i * d))
    return my_list

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

new_list = fill_array(a1, d, n)
print(new_list)
