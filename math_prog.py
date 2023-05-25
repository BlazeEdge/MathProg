# Math prog
import time
import os
# Импорты


os.system('cls')
print("___________________________")
print("|Math_prog                |")
print("|                         |")
print("|   Добро пожаловать!!!   |")
print("|                         |")
print("|_________________________|")

print('Загрузка меню...')
time.sleep(2.5)
# Загрузочное меню

while True:
    os.system('cls')
    print()
    print('____________________________')
    print('|Math_prog                 |')
    print('|1) Прямоугольник          |')
    print('|2) Треугольник            |')
    print('|3) Дополнительно          |')
    print('|__________________________|')
    print('|0) Информация о программе |')
    print('|__________________________|')
    print('|exit - Выход              |')
    print('|__________________________|')
    print()
    menu = input('>>> ')
    os.system('cls')
    

    if menu == '1':
        print()
        print('________________________________________')
        print('|Math_prog                             |')
        print('|1) Периметр прямоугольника            |')
        print('|2) Площадь прямоугольника             |')
        print('|                                      |')
        print('|______________________________________|')
        print()
        menu0 = input('>>> ')

        if menu0 == '1':
            print('_________________________')
            print('|Периметр прямоугольника|')
            print('|_______________________|')
            print()
            a = int(input('Введите длину 1-й стороны: >>> '))
            b = int(input('Введите длину 2-й стороны: >>> '))
            awsner = (a+b)*2
            print(f'Периметр прямоугольника: {awsner}')
            os.system('pause')

        elif menu0 == '2':
            print('_________________________')
            print('|Площадь прямоугольника |')
            print('|_______________________|')
            print()
            a = int(input('Введите длину 1-й стороны: >>> '))
            b = int(input('Введите длину 2-й стороны: >>> '))
            awsner = a*b
            print(f'Площадь прямоугольника: {awsner}')
            os.system('pause')

    elif menu == '2':
        print()
        print('________________________________________')
        print('|Math_prog                             |')
        print('|1) Периметр треугольника              |')
        print('|2) Площадь треугольника               |')
        print('|                                      |')
        print('|______________________________________|')
        print()
        menu1 = input('>>> ')

        if menu1 == '1':
            print('_________________________')
            print('|Периметр треугольника  |')
            print('|_______________________|')
            print()
            a = int(input('Введите длину 1-й стороны: >>> '))
            b = int(input('Введите длину 2-й стороны: >>> '))
            c = int(input('Введите длину 3-й стороны: >>> '))
            awsner = a+b+c
            print(f'Периметр прямоугольника: {awsner}')
            os.system('pause')

        elif menu1 == '2':
            print('_________________________')
            print('|Площадь треугольника   |')
            print('|_______________________|')
            print()
            b = int(input('Введите длину основания треугольника: >>> '))
            h = int(input('Введите высоту треугольника: >>> '))
            awsner = S=0.5*b*h
            print(f'Площадь треугольника: {awsner}')
            os.system('pause')

    elif menu == '3':
        print()
        print('_________________________________________')
        print('|Math_prog                              |')
        print('|1) Калькулятор                         |')
        print('|2) Вычисление корня уравнения          |')
        print('|                                       |')
        print('|_______________________________________|')
        print()
        menu2 = input('>>> ')

        if menu2 == '1':
            print('_________________________')
            print('|Калькулятор            |')
            print('|_______________________|')
            calculator = eval(input('\n>>> '))
            print(f'Решение: {calculator}')
            os.system('pause')

        if menu2 == '2':
            print('____________________________')
            print('|Вычисление корня уравнения|')
            print('|__________________________|')
            print('|1) x+a=b                  |') # b-a
            print('|2) x-a=b                  |') # a-b
            print('|3) a-x=b                  |') # a-b
            print('|4) x*a=b                  |') # b/a
            print('|5) x/a=b                  |') # a*b
            print('|6) a/x=b                  |') # a/b
            print('|__________________________|')
            equation = input('Выберите вид уравнения\n>>> ')

            if equation == '1':
                a = int(input('Введите значение a\n>>> '))
                b = int(input('Введите значение b\n>>> '))
                x = b-a
                print(f"Значение x: {x}")
                os.system('pause')

            elif equation == '2':
                a = int(input('Введите значение a\n>>> '))
                b = int(input('Введите значение b\n>>> '))
                x = a-b
                print(f"Значение x: {x}")
                os.system('pause')

            elif equation == '3':
                a = int(input('Введите значение a\n>>> '))
                b = int(input('Введите значение b\n>>> '))
                x = a-b
                print(f"Значение x: {x}")
                os.system('pause')

            elif equation == '4':
                a = int(input('Введите значение a\n>>> '))
                b = int(input('Введите значение b\n>>> '))
                x = b/a
                print(f"Значение x: {x}")
                os.system('pause')

            elif equation == '5':
                a = int(input('Введите значение a\n>>> '))
                b = int(input('Введите значение b\n>>> '))
                x = a*b
                print(f"Значение x: {x}")
                os.system('pause')

            elif equation == '6':
                a = int(input('Введите значение a\n>>> '))
                b = int(input('Введите значение b\n>>> '))
                x = a/b
                print(f"Значение x: {x}")
                os.system('pause')

    elif menu == '0':
        print()
        print('_________________________________')
        print('|1) Разработчик - blaze_edge    |')
        print('|2) Discord - blaze_edge#7221   |')
        print('|3) VK - blaze_edge             |')
        print('|4) Версия - 0.0.3 alpha        |')
        print('|5) Обновлён список поддерживае-|')
        print('|мых уравнений                  |')
        print('|_______________________________|')
        print('|      Math_Prog - 2023         |')
        print('|_______________________________|')
        print()
        os.system('pause')

    elif menu == 'exit':
        quit()
    # Попытка выхода