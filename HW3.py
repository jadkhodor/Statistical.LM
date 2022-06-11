import random

#defining
n_dice = sorted(list(range(1, 7)))

sum_n_dice = sorted(list(d1 + d2 for d1 in n_dice for d2 in n_dice))

tested_combos = list()

max_dice_v = 10

found = False

max_iter = 10 ** 10

#code

for i in range(0, max_iter):
    new_dice1 = [1]
    new_dice2 = [1]
    while len(new_dice1) < 6 and len(new_dice2) < 6:
        new_dice1.append(random.randint(2, max_dice_v))
        new_dice2.append(random.randint(2, max_dice_v))

    new_dice1.sort()
    new_dice2.sort()

    #checks

    if new_dice1 == n_dice or new_dice2 == n_dice or max(new_dice1) + max(new_dice2) > 12:
        continue

    if [new_dice1, new_dice2] in tested_combos or [new_dice2, new_dice1] in tested_combos:
        continue

    sum_new_dice = sorted(list(d1 + d2 for d1 in new_dice1 for d2 in new_dice2))


    if sum_n_dice == sum_new_dice:
        print("\n Sicherman dices found! \n 1st Dice : " + new_dice1.__str__() + "\n 2nd Dice: " + new_dice2.__str__())
        found = True
        break

    tested_combos.append([new_dice1, new_dice2])

if found == False:
   print("No Dice found!")