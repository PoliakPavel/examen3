# Напишите функцию, которая проверяет: является ли слово палиндромом

def pol(n):
    return n == n[::-1]


print(pol('шалаш'))