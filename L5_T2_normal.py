import L5_T1_easy
import os


def change_dir(path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return 'dir_{} - папки не существует'.format(path)


def start():
    answer = ''
    while answer != '5':
        print('Текущая папка: ' + os.getcwd())
        answer = input('Выберите действие:\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать новую папку\n'
                       '5. Выход\n')
        if answer == '5':
            break
        if answer == '1':
            path_name = input('Укажите папку для перехода: ')
            print(change_dir(path_name))
        elif answer == '2':
            x = os.listdir()
            for i in x:
                print(i)
        elif answer == '3':
            name = input('Введите имя удаляемой папки: ')
            L5_T1_easy.delete_dir(name)
        elif answer == '4':
            name = input('Введите имя новой папки: ')
            L5_T1_easy.new_dir(name)


if __name__ == '__main__':
    start()
