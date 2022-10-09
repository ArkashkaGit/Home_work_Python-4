# Задача 31 :	
# Задайте натуральное число N. 
# Напишите программу, 
# которая составит список простых множителей числа N.
# пример: 
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]


number = int(input("Введите натуральное число:\n"))
i = 2 
list_prime_number = []

while i <= number:
    if number % i == 0:
        list_prime_number.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители заданного числа: {list_prime_number}")