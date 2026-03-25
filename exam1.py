import sys


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def set_exit(self, direction, room):
        self.exits[direction] = room


class Player:
    def __init__(self, current_room, energy=100):
        self.current_room = current_room
        self.energy = energy
        self.inventory = []

    def move(self, direction):
        if direction not in self.current_room.exits:
            print(f'Туда нельзя идти! Доступные выходы: {list(self.current_room.exits.keys())}')
            return

        next_room = self.current_room.exits[direction]

        if next_room.name == 'сад':
            has_key = False
            for item in self.inventory:
                if item.name == 'ключ':
                    has_key = True
                    break

            if not has_key:
                print('Дверь в сад заперта! Вам нужен ключ в инвентаре кажется, он был на кухне.')
                return

        if self.energy >= 10:
            self.current_room = next_room
            self.energy -= 10
            print(f'\nВы перешли в: {self.current_room.name}')
            print(f'Описание: {self.current_room.description}')
        else:
            print('Вы слишком устали. Игра окончена.')

    def take_item(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.inventory.append(item)
                self.current_room.items.remove(item) # удалеть эз румы чтобы не поднять его еще раз
                print(f'подобран: {item_name}')
                return
        print('Такого предмета здесь нет.')


class Item:
    def __init__(self, name):
        self.name = name


room1 = Room('кухня', 'тут пахнет пирожками, на столе крошки и ключ.')
room2 = Room('коридор', 'длинный темный коридор.')
room3 = Room('сад', 'цветочкэ')
ключ = Item('ключ')
room1.items.append(ключ)

# соединяем комнаты (из кухни на север - коридор, из коридора на юг - кухня
room1.set_exit('север', room2)
room2.set_exit('юг', room1)
room2.set_exit('восток', room3)
room3.set_exit('запад', room2)

hero = Player(room1)
energy = 100

print('игра запущена')
print(f'начало в локации: {hero.current_room.name}')

# game cycle

while True:
    print(f'\n сейчас вы здесь: {hero.current_room.name}')
    print('энергия = ',  hero.energy)
    print('Команды: север, юг, запад, восток, выход, взять')

    choice = input("куда идем? -->").strip().lower()

    if choice == 'выход':
        print('игра завершена. Пока!')
        break
    elif choice.startswith('взять '):
        item_to_take = choice.replace('взять ', '')
        hero.take_item(item_to_take)

    elif choice in ['север', 'юг', 'запад', 'восток']:
        hero.move(choice)

        if hero.energy < 10:
            print("Вы слишком устали и упали без сил. Конец игры!")
            break
    else:
        print('Неизвестна команда. Попробуй "север" или "юг".')
