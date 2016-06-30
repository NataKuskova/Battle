import random


class Unit:
    health = None
    recharge = None

    def __init__(self, health, recharge):
        self.health = health
        self.recharge = recharge

    def do_attack(self):
        # атака
        pass

    def take_damage(self, *args):
        # получение атаки и блок
        pass

    def get_recharge(self):
        return self.recharge

    def get_health(self):
        return self.health


class Solder(Unit):
    recharge = random.randint(100, 2000)
    experience = 0
    health = 100

    def get_experience(self):
        return self.experience

    def do_attack(self):
        soldiers_attack = 0.5 * (1 + self.get_health() / 100) * \
                          random.randint(50 + self.experience, 100) / 100
        attack = self.take_damage(soldiers_attack)
        self.health -= attack

    def take_damage(self, attack):
        damage = 0.05 + self.experience / 100
        return attack - damage


class Vehicles(Unit):
    recharge = random.randint(1000, 2000)
    operators = []
    health = None

    def __init__(self):
        super().__init__(self.health, self.recharge)
        operator_count = random.randint(1, 3)
        i = 0
        while i < operator_count:
            self.operators.append(Solder(Solder.health, Solder.recharge))

    def get_operators(self):
        return self.operators

    def set_health(self):
        # for i in self.operators:
            # i.health += i.health
        pass


class Squad:
    units = None

    def __init__(self, units):
        self.units = units

    def get_power(self):
        pass


if __name__ == "__main__":
    pass
