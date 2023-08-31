import random

class Dice:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)



def main():

    dice = Dice()

    print(dice.roll())
    print(dice.roll())

    d20 = Dice(20)

    for r in range(100):
        print(d20.roll())


main()