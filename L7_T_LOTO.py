import copy
import random

Max_Casks = 90
Card_digits = 15
Line_digits = 5


def gen_card():
    the_matrix = random.sample(range(1, Max_Casks + 1), Card_digits)
    card = [sorted(the_matrix[i:i + Line_digits]) for i in range(0, len(the_matrix), Line_digits)]
    return card


def gen_casks_list():
    return random.sample(range(1, Max_Casks + 1), 90)


def get_cask(cask_list):
    return cask_list.pop()


def show_card(card):
    card = copy.deepcopy(card)
    placeholders = ' '.join(['{:>2}' for i in range(9)])
    for line in card:
        for space in ' ' * 4:
            line.insert(random.randint(0, len(line) - 1), space)
    return [placeholders.format(*line) for line in card]


def update_card(card, cask):
    for line in card:
        yield ['-' if x == cask else x for x in line]


def is_empty(card):
    for line in card:
        for elm in line:
            if elm != '-':
                return False
    return True


def cask_in_card(card, cask):
    return cask in [cask for line in card for cask in line]


def play_round():
    print('''Добро пожаловать в игру ЛОТО. Вы будете играть с компьютером. Удачи!\n''')
    player_card, comp_card = gen_card(), gen_card()
    casks = gen_casks_list()
    while True:
        next_cask = get_cask(casks)
        print('Выпал бочонок: {}. В мешке осталось: {}'.format(next_cask, len(casks)))
        print("{0} Ваш билет {0}\n{1}\n{2}\n{3}".format('-' * 6, *show_card(player_card)))
        print("{0} Билет компьютера {0}\n{1}\n{2}\n{3}".format('-' * 5, *show_card(comp_card)))
        answ = 'a'
        while answ not in 'ynq':
            answ = input("Бочонок есть в Вашем билете? y/n или q если Вам надоело: ")
        if answ == 'q':
            break
        elif (answ == 'y' and cask_in_card(player_card, next_cask)) or (answ == 'n' and not cask_in_card(player_card,
                                                                                                         next_cask)):
            print("Все верно! \n\nСледующий ход...")
        else:
            print("Вы проиграли!")
            break
        player_card = list(update_card(player_card, next_cask))
        comp_card = list(update_card(comp_card, next_cask))
        if is_empty(player_card):
            print('Ваш билет выйгрышный! Подождите 5 минут - выйгрыш печатается.')
            break
        if is_empty(comp_card):
            print('Копьютеру повезло! Джек пот не разыгран.')
            break


play_round()
