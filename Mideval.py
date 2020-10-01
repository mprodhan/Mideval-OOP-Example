import sys


class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attackin with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        User.attack(self)
        print(f'attacking with arrows - {self.arrows} arrows left.')


Merlin = Wizard('Merlin', 60)
GreenArrow = Archer('Oliver', 1000)
sys.setrecursionlimit(10**3) 

for char in [Merlin, GreenArrow]:
    char.attack()
# def player_attack(char):
#     char.attack()

# player_attack(Merlin)
# player_attack(GreenArrow)

# print(Merlin.attack())
# print(GreenArrow.attack())

