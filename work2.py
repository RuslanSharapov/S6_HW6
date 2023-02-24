#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)



def find_indices_in_range(arr, mini, maxi):
    indices = []
    for i, val in enumerate(arr):
        if mini <= val <= maxi:
            indices.append(i)
    return indices

my_list = [3, 7, 15, 20, 30, 45]
indices = find_indices_in_range(my_list, 8, 20)
print(indices)


""" my_list = [3, 7, 15, 20, 30, 45]
indices = [i for i, x in enumerate(my_list) if 10 <= x <= 20]
print(indices) """
