import random
fighter = {"health": 5, "attack": 3, "dodge": 1}
thief = {"health": 2, "attack": 3, "dodge": 4}
mage = {"health": 1, "attack": 5, "dodge": 4}
types = {"fighter": fighter, "thief": thief, "mage": mage}
class Characters():
    _health = 0
    _attack = 0
    _dodge = 0
    def __init__(self, char_type):
        self._char_type = char_type
        self._assign_attributes()
    def __str__(self):
        return self._char_type
    def _assign_attributes(self):
        types_dict = types[self._char_type]
        self._health = types_dict['health']
        self._attack = types_dict['attack']
        self._dodge = types_dict['dodge']
    def attack(self):
        return self._attack
    def take_damage(self, damage):
        if self.dodge_success():
            return "Miised!"
        self._health -= damage
        return f'{self._char_type} took {damage} damage.'

    def dodge_success(self):
        rand = random.randint(0,100)
        self.hit = False
        if self._dodge*5 <= rand:
            return True
        else: return False


    def is_dead(self):
        return self._health < 1
def character_fight(type1, type2):
    character1 = Characters(type1)
    character1 = Characters(type1)
    coin_toss = random.randint(0,1)
    if

'''Класс имеет следующие методы:
Распределение атрибутов как описано выше: character_1 = Character("fighter")
Атака
Получение урона в случае если увернуться не удалось.
Уклонение: каждое очко уклонения умножается на 5. Результат уклонения зависит от рандомно генерируемого числа
от 0 до 100. Если это число меньше или равно навыка уклонения, то герой уклоняется от атаки.
Смерть: если здоровье меньше 1.

Напишите функцию которая заставит сразиться разных героев друг с другом 100 раз. Выведите счет.
'''