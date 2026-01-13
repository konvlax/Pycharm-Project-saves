# class Cat:
#     # метод __init__ - конструктор, вызывается при создании обьекта
#     def __init__(self, name):
#         self.name = name                            # Атрибут обьекта
#
#     def speak(self):
#         return f"{self.name} стал бррррррр бррррр патапимммом"
#
# # создание объекта (экземпляра класса)
#
#
# my_cat = Cat('Мурчик')
#
# # вызов метода объекта
# print(my_cat.speak())   # выведет: Мурчик издает какой-то звук
# # изменение атрибута объекта
# my_cat.name = "Барсик"
#
#
# class Zombe:
#     def __init__(self, name):
#         self.name = name
#         self.health = 50
#
#
#     def growl(self):
#         return f"{self.name} рычит: не чиназэс"
#
#
# zombe1 = Zombe('кровав')
# zombe2 = Zombe("не кровав")
# print(zombe1.name)
# print(zombe2.name)
# print(zombe1.health)
# print(zombe1.growl())
# играааа 1 зондбе
print("🕹 === БИТВА ГЕРОЕВ === \n")


# 🏭 КЛАСС 1: ЧЕРТЕЖ ГЕРОЯ (класс = шаблон)
class Char:
    def __init__(self, name, health=100, max_health=None, damage=20):
        self.name = name
        self.health = health
        self.max_health = max_health or health
        self.damage = damage        # ✅ Добавили урон герою

    def status(self):
        percent = (self.health / self.max_health) * 100
        return f"{self.name}: {self.health} / {self.max_health} HP ({percent:.0f}%) | Урон: {self.damage}"

    def attack(self, target):
        return f"{self.name} бьет {target.name} на {self.damage} !"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f"{self.name} получил {damage} урона. Осталось: {self.health} HP"

    def is_alive(self):
        return self.health > 0


class Enemy:
    def __init__(self, name, health=60, damage=15):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = health

    def status(self):
        percent = (self.health / self.max_health) * 100
        return f"{self.name}: {self.health}/{self.max_health} HP ({percent:.0f}%) | Урон: {self.damage}"

    def attack(self, target):
        return f"{self.name} бьёт {target.name} на {self.damage}"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f'{self.name} получил {damage}! Осталось: {self.health} HP'

    def is_alive(self):
        return self.health > 0


print('собираем армию по чертежам... \n')


# Создаем объекты (фигурки) по чертежам
hero = Char('🛡 Артур', 120, damage=25)
creep = Enemy("☠ крип", 50, 12)
boss = Enemy("🐷 пудж", 200, 30)
army = [hero, creep, boss]
print("Состав мид лайна:")
for unit in army:
    print(unit.status())

print("\n" + "="*50 + "\n")

# Боевая система


def battle_round(attacker, defender):
    """Один раунд боя"""
    print(f"\n 🔥🔥🔥 РАУНД:")
    print(attacker.status())
    print(defender.status())

    # АТАКА
    print(attacker.attack(defender))
    print(defender.take_damage(attacker.damage))

    print(defender.status())
    print("-"*30)

# БИТВАААА


print('начинается битва! \n')
battle_round(creep, hero)
battle_round(hero, creep)
battle_round(boss, hero)
battle_round(hero, boss)

print("\n" + "="*50 + "\n")

print(" ИТОГИ ")
for unit in army:
    status = unit.status()
    if not unit.is_alive():
        status += "ПОТРАЧЕНО"
    print(status)


print("=== КОНЕЦ ДЕМОНСТРАЦИИ ООП ===")
print("Классы = чертежи")
print('Объекты = фигурки')
print('Методы = умения')
print('Атрибуты = характеристики (урон, здоровье')
print("готово к уроку - тестировано!")