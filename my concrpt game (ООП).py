print('игра в жанре рпг в жанре темного фентези (типа Skyrim, Morrowind. '
      'Игрок линейно путешествует, встречая разных союзников/врагов и получая новое оружие')


class Skeleton:
    def __init__(self, name, health=30, max_health=None, damage=13):
        self.name = name
        self.health = health
        self.max_health = max_health or health
        self.damage = damage

        
class Vampire:
    def __init__(self, name, health=70, max_health=None, damage=20):
        self.name = name
        self.health = health
        self.max_health = max_health or health
        self.damage = damage



enemies = [Skeleton]
