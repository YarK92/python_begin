# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заново.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

x = int(input('Введите число: '))
while not 10 > x > 0:
    print('Вы ввели неверное число. Введите число от 1 до 9')
    x = int(input('Введите число согласно вышеуказанным требованиям: '))
else:
    print("Ваше число в квадрате будет равно:", x ** 2)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

x = x + y
y = x - y
x = x - y

print('Я поменял их местами !', 'Первое число теперь: ', x, 'Второе число теперь: ', y)
