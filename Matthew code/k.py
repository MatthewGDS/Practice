import random
numberOfStreaks = 0
HeadRow = 0
TailsRow = 0

heads = [0, 0, 0, 0, 0, 0]
tails = [1, 1, 1, 1, 1, 1]
set = []

for experimentNumber in range(10000):

    randnum = random.randint(0, 1)

    if randnum == 0:
        print("head")
        head = True
    else:
        print("tails")
        head = False
        
    if head:
        if 1 in set:
            set = []
        if randnum == 0:
            set.append(0)
    else:
        if 0 in set:
            set = []
        if randnum == 1:
            set.append(1)

    if set == heads:
        HeadRow += 1
        numberOfStreaks += 1
    if set == tails:
        TailsRow += 1
        numberOfStreaks += 1

print("Heads = " + str(HeadRow))
print("Tails = " + str(TailsRow))
print("#Streaks = " + str(numberOfStreaks))
    



