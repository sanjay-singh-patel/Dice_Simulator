import random


# Class for a dice

class Dice:

    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self) -> int:
        self.value = random.randint(1, 6)
        return self.value


#object declaration and driving code


my_dice = Dice()
while 1:
    print("press 1 to roll the dice\npress 0 to quit")
    if int(input()) == 1:
        print(int(my_dice.roll()))
    else:
        break
