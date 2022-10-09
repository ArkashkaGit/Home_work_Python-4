# Задача 33 :	
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# 1.	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def new_writeite_file(st):
    with open('file_1.txt', 'w') as data:
        data.write(st)

def rand():
    return random.randint(0,101)

def create_mn(k):
    new_spisok = [rand() for i in range(k+1)]
    return new_spisok
    
def create_str(sp):
    new_spisok= sp[::-1]
    new_write = ''
    if len(new_spisok) < 1:
        new_write = 'x = 0'
    else:
        for i in range(len(new_spisok)):
            if i != len(new_spisok) - 1 and new_spisok[i] != 0 and i != len(new_spisok) - 2:
                new_write += f'{new_spisok[i]}x^{len(new_spisok)-i-1}'
                if new_spisok[i+1] != 0:
                    new_write += ' + '
            elif i == len(new_spisok) - 2 and new_spisok[i] != 0:
                new_write += f'{new_spisok[i]}x'
                if new_spisok[i+1] != 0:
                    new_write += ' + '
            elif i == len(new_spisok) - 1 and new_spisok[i] != 0:
                new_write += f'{new_spisok[i]} = 0'
            elif i == len(new_spisok) - 1 and new_spisok[i] == 0:
                new_write += ' = 0'
    return new_write

n = int(input("Введите натуральную степень k = "))
result = create_mn(n)
new_writeite_file(create_str(result))