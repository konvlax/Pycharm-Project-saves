import time

# --- 1. база ---


class Sim:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 100
        self.is_alive = True

    def eat(self):
        if self.hunger >= 100:
            print(f"{self.name} не хоча ести")
        else:
            self.hunger += 20
            self.energy -= 5
            print(f"{self.name} поел(а). Голод: {self.hunger}")

    def live_day(self):
        self.hunger -= 10
        self.energy -= 10
        if self.hunger <= 0 or self.energy <= 0:
            self.is_alive = False
            print(f"{self.name} не выдержал и покинул мир. F.")

    def status(self):
        return f"{self.name} | голод: {self.hunger} | энергия: {self.energy}"


# --- 2. Классы наследники ---

class Human(Sim):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job
        self.money = 50

    def work(self):
        self.energy -= 30
        self.hunger -= 20
        self.money += 100
        print(f"{self.name} сходил на работу ({self.job}). +100$. Энергия: {self.energy}")

    def feed_pet(self, pet):
        if self.money >= 20:
            print(f"{self.name} покупает корм и кормит {pet.name}")
            self.money -= 20
            pet.eat()
        else:
            print(f"{self.name}, обеднел. Денег не хватает.")

    def repair_robot(self, robot):
        print(f"{self.name} чинит {robot.name}")
        self.energy -= 20
        robot.energy = 100
        print(f"{robot.name} заряжен!")

    def feed_homeless(self, homeless):
        print(f"Привет, {homeless.name}!")
        self.money -= 5
        homeless.hunger += 50


class Dog(Sim):
    def eat(self):
        self.hunger += 30
        print(f"{self.name} поела")

    def play(self, human):
        print(f"{self.name} приносит мячик {human.name}")
        self.energy -= 20
        human.energy += 10
        print(f"{human.name} повеселел")


class Robot(Sim):
    def __init__(self, name):
        super().__init__(name)
        self.battery = 100

    def live_day(self):
        self.energy -= 5

    def eat(self):
        print("f{self.name} на розетке")
        self.energy = 100

    def cook_dinner(self, human):
        if self.energy > 20:
            print(f"{self.name} готовит ужин дл {human.name}.")
            self.energy -= 20
            human.eat()
        else:
            print(f"{self.name} разрядился :(")


class Homeless(Sim):
    def anger(self, human):
        if self.hunger <= 20:
            print(f"{player.name}, делись едой! 😡💢")
            human.energy -= 20
            human.money -= 50

    def live_day(self):
        self.hunger -= 7


# --- 3. игровой мир ---

player = Human("алекс", "программист")
doggo = Dog("боб")
robo = Robot("Валера")
mike = Homeless("майк")

household = [player, doggo, robo, mike]
day = 1
print("Игра начинается 🚲🚲🚲")

# --- 4. цикл (game loop) ---
while True:
    print(f"\n=== День {day} ===")

    game_over = False
    for sim in household:
        if sim not in household:
            if not sim.is_alive:
                print(f"Потрачено: {sim.name} *YOU DIED* ")
    if game_over:
        break
    if mike.hunger <= 20:
        mike.anger(player)
    print(f"Деньги: {player.money}$")

    for sim in household:
        print(sim.status())

    print("\n Что будет делать Алекс?")
    print("1. Пойти на работу")
    print("2. Поесть самому (-20$ еда)")
    print("3. Покормить Бобика (-20$ корм)")
    print("4. Поиграть с Бобиком")
    print("5. Попросить приготовить робота ужин")
    print("6. Починить робота")
    print("7. Покормить бездомного")
    print("0. Выход")

    choice = input("Твой выбор: ")

    if choice == "1":
        player.work()
    elif choice == "2":
        if player.money >= 20:
            player.money -= 20
            player.eat()
        else:
            print("Бедность !")
    elif choice == "3":
        player.feed_pet(doggo)
    elif choice == "4":
        doggo.play(player)
    elif choice == "5":
        robo.cook_dinner(player)
    elif choice == "6":
        player.repair_robot(robo)
    elif choice == "7":
        player.feed_homeless(mike)

    elif choice == "0":
        print('ББ')
        break
    else:
        print("По кнопочкам следует попадать")

    print("\n наступает ночь. Все показатели упали.")
    time.sleep(1)
    for sim in household:
        sim.live_day()

    day += 1
