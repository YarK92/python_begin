# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
#
import math

list_1 = [i for i in range(-10, 11)]
list_2 = [j ** 2 for j in list_1]
print(list_2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
list_1 = ["персик", "груша", "абрикос", "слива", "земляника", "малина"]
list_2 = ["персик", "абрикос", "земляника", "крыжовник", "нектарин", "яблоко", "черника"]
list_3 = [i for i in list_1 for l in list_2 if i == l]
print(list_3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list_1 = [i for i in range(-100, 101)]
list_2 = [j for j in list_1 if j > 0 and j % 3 == 0 and j % 4 != 0]
print(list_2)