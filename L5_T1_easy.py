# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
import shutil


def new_dir(i):
    os.mkdir('{}'.format(i))


def delete_dir(i):
    os.rmdir('{}'.format(i))


for r in range(9):
    new_dir('dir_{}'.format(r + 1))
for r in range(9):
    delete_dir('dir_{}'.format(r + 1))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
'''def cur_dir():
    x = os.listdir()
    for index, element in enumerate(x, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))'''

x = os.listdir()
for i in x:
    print(i)




# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def backup_file():
    file = os.path.realpath(__file__)
    file_bup = file + '.copy'
    if not os.path.isfile(file_bup):
        shutil.copy(file, file_bup)
        return file_bup + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(backup_file())
