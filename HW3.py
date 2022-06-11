from random import randint
from math import factorial

standard_dice = sorted(list(range(1, 7)))
sums_standard_dice = sorted(list(a + b for a in standard_dice for b in standard_dice))

max_value = 12

# Number of possible combinations of selecting 12 (as we have 2 dices with 6 sides each)  values out of 13 possible
# values (0-12), replacement allowed. I find this as a number small enough to check all the possibilies.
max_iterations = int(factorial(max_value + 12) / (factorial(12) * factorial(max_value)))

for i in range(max_iterations):

    new_dice1 = sorted(list(randint(0, max_value) for i in range(6)))
    new_dice2 = sorted(list(randint(0, max_value) for i in range(6)))

    if new_dice1 == standard_dice or new_dice2 == standard_dice or max(new_dice1) + max(new_dice2) > max_value + 1:
        continue

    sums_new_dice = sorted(list(a + b for a in new_dice1 for b in new_dice2))

    if sums_standard_dice == sums_new_dice:
        print("Found an example o f Sichemarn dices! They are:\n" + new_dice1.__str__() + "\n" + new_dice2.__str__())
        break
    if i == max_iterations - 1:
        print("Schimerman dices doesn't exist!")