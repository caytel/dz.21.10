"""
Написать программу, которая переводит число из десятчной системы счисления в двоичную или восьмеричную (по указанию пользователя)
"""
while True:
    try:
        n10 = int(input("Введите целое число: "))
        system = int(input("Введите целевую систему счисления: "))
        break
    except (TypeError, ValueError):
        print ('Это не целое число, пожалуйста, введите целое число')

def binar(n):
    n2 = ''
    while n > 0:
        n2 = str(n % 2) + n2
        n//=2
    return n2
    
def octal(n):
    n8 = ''
    while n > 0:
        n8 = str(n % 8) + n8
        n//=8
    return n8

if system == 2:
    print("Вывод: ", n10, "->", binar(n10))
elif system == 8:
    print("Вывод: ", n10, "->", octal(n10))
else: 
    print("Перезапустите программу ")