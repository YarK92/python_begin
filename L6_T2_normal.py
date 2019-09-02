# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random


class Person:
    def __init__(self, name, health, armour, damage):
        self.name = name
        self.health = health
        self.armour = armour
        self.damage = damage

    def __damage(self, damage):
        if self.armour > 0:
            self.armour = self.armour - int(damage * random.uniform(0.1, 1.0))
            if self.armour <= 0:
                self.armour = 0
        else:
            self.health = self.health - int(damage * random.uniform(0.1, 1.0))
            if self.health <= 0:
                self.health = 0

        print('{} получил урон и теперь имеет {} здоровья, {} брони'.format(self.name, self.health, self.armour))

    def the_hit(self, person):
        person.__damage(self.damage)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self, player1, player2):
        while player1.health > 0 and player2.health > 0:
            player1.the_hit(player2)
            if player2.health == 0:
                print('{} победил!'.format(player1.name))
                break
            player2.the_hit(player1)
            if player1.health == 0:
                print('{} победил!'.format(player2.name))


player = Player(input('Введите Ваше имя: '), 100, random.randint(30, 50), random.randint(2, 10))
enemy = Enemy(input('Позвольте второму игроку ввести имя: '), 100, random.randint(30, 50), random.randint(2, 10))

new_fight = Battle(player, enemy)
new_fight.start(player, enemy)
