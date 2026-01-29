import time
import random

# --- 1. БАЗОВЫЙ КЛАСС (Основа для всех) ---
polytion_chance = 10

class Resident:

    def __init__(self, name):
        self.name = name
        self.hunger = 60
        self.energy = 80
        self.is_alive = True

    def status(self):
        return f"{self.name} | 🍗 Голод: {self.hunger} | ⚡️ Энергия: {self.energy}"

    def live_day(self):
        """Пассивное старение/усталость (базовая логика)"""
        self.hunger -= 15
        self.energy -= 15
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False

    def react_to_mess(self):
        """Пример полиморфизма: каждый житель по-разному реагирует на хлам"""
        pass

    def polytion(self):
        


class WorkerSim(Resident):
    def __init__(self, name, money):
        super().__init__(name)
        self.money = money

    def work(self):
        print(f'{self.name} ушел на заработки в Сибирь')
        self.money += 150
        self.energy -= 30
        self.hunger -= 20

    def react_to_mess(self):
        print(f'{self.name}: Как в свинарнике! -10 энергии')
        self.energy -= 10


class LazySim(Resident):
    def __init__(self, name):
        super().__init__(name)
        self.laziness = 100

    def live_day(self):
        self.hunger -= 5
        self.energy -= 5
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False

    def sleep_on_trash(self):
        print(f'{self.name} прилег на мусор')
        self.energy += 40
        self.hunger -= 5

    def react_to_mess(self):
        print(f'{self.name}: Какой мусор? Это просто помои')


worker = WorkerSim('работяга Петрович', 100)
lazy_guy = LazySim('Ларри (ленивец)')
roommates = [worker, lazy_guy]
day = 1
is_messy = True
print('СИМУЛЯТОР КОММУНАЛКИ ЗАПУЩЕН')

while True:
    print(f"\n=== День {day} ===")

    if not all(r.is_alive for r in roommates):
        dead = next(r for r in roommates if not r.is_alive)
        print(f"конец игры. {dead.name} покинул этот мир")

    print(f"Деньги Петровича: {worker.money} | Состояние: {'ХЛАМ' if is_messy else 'Чисто'}")
    for r in roommates:
        print(r.status())

    print('\n ВАШ ВЫБОР')
    print('1. Петрович: Пойти на работу (+150$)')
    print("2. Петрович: Купиц пиццу на всех (-50$)")
    print("3. Ларри: Поспать в куче хлама (+энергия)")
    print("4. Ларри: Попросить у Петровича денег на еду")
    print("5. Убраться в комнате (Петрович теряет энергию)")
    print("0. Выход")
    choice = input('Действие: ')
    if choice == '1':
        worker.work()
    elif choice == '2':
        if worker.money >= 50:
            worker.money -= 50
            worker.energy += 50
            for r in roommates:
                r.hunger += 40

            print('Все поели')
        else:
            print('ноу мани')
    elif choice == '3':
        if is_messy:
            lazy_guy.sleep_on_trash()
        else:
            print('Хлама нет, сплю на полу')
            lazy_guy.energy += 10
    elif choice == '4':
        print(f'ларри клянчит деньги. Петрович в ярости.')
        worker.energy -= 5
    elif choice == '5':
        print('Петрович вынес весь мусор Лари')
        is_messy = False
        worker.energy -= 30
    elif choice == "0":
        break
    print('ночь в коммуналке')
    time.sleep(1)
    for r in roommates:
        r.live_day()
        if is_messy:
            r.react_to_mess()

    day += 1
print('игра завершена')