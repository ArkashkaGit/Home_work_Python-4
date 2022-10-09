# Задача 32 :	
# Задайте последовательность чисел. 
# Напишите программу, 
# которая выведет список неповторяющихся 
# элементов исходной последовательности.

list_element = [1,2,'a',3,4,4,5,4,'b',7,'a']
unique_lust = set(list_element)

print(list_element)
print(unique_lust)

#-------------------------------------

massiv = list(map(int, input("Введите числа через запятую:\n").split(",")))
exclusive_numbers = []

for i in massiv:
    if i not in exclusive_numbers:
        exclusive_numbers.append(i) 
# [new_list.append(i) for i in massiv if i not in exclusive_numbers]
print(f"Cписок massiv: {massiv}")
print(f"Список из неповторяющихся элементов: {exclusive_numbers}")