class Sim:
    def __init__(self, name, energy=50):
        self.name = name
        self.energy = energy


class Bed:
    @staticmethod
    def use_for_sleep(sim):
        sim.energy = 100


a = input()
my_sim = Sim(name=a)
my_bed = Bed()
my_bed.use_for_sleep(my_sim)
print(f"Энергия сима {my_sim.name} теперь {my_sim.energy}")


class Home:
    def __init__(self, name):
        self.name = name

    def sleep(self, sim):
        print(f"{sim.name} спит в доме {self.name}")
        sim.energy += 20

    def relax(self, sim):
        print(f"{sim.name} отдыхает")
        sim.energy += 10


class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

    def work_in_kfc(self, sim):
        print(f"{sim.name} работает как {self.title}")
        sim.money += self.salary
        sim.energy -= 15

    def work_as_gamer(self, sim):
        print(f"{sim.name} работает как {self.title}")
        sim.money += self.salary
        sim.energy -= 5


class Sim:
    def __init__(self, name, home, job, happieness=50):
        self.name = name
        self.energy = 50
        self.money = 100
        self.home = home
        self.job = job
        self.happieness = happieness

    def eat(self):
        print(f"{self.name} ест")
        self.energy += 10
        self.money -= 5

    def show_status(self):
        print('------')
        print(f'имя:{self.name}')
        print(f"энергия: {self.energy}")
        print(f"деньги: {self.money}")
        print(f"счастье = {self.happieness}")
        if sim.energy <= 0:
            print('сим устал')
        if sim.money <= 0:
            print('сим обеднел')


class Pet:
    def __init__(self, name):
        self.name = name

    def pet(self):
        print(sim.name, f"гладит {self.name}")
        sim.happieness += 5




b = input()
my_pet = Pet(name=b)
home = Home('уютный дом')
job = Job("геймер", 30)
sim = Sim(a, home, job)
sim.show_status()
sim.job.work_as_gamer(sim)

sim.home.sleep(sim)
sim.eat()
Pet.pet(my_pet)
sim.show_status()

