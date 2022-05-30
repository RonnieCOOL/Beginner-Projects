import random

lst = ["Snake", "Water", "Gun"]

count_me = 0
count_pc = 0
count = 10

while(count != 0):
    choice = random.choice(lst)
    s = str(input("Type 'S' for Snake, 'W' for Water and 'G' for Gun : "))

    if(choice == "Snake"):
        if(s == "W"):
            count_pc += 1
            print("PC gets 1 point\n")
        elif (s == "G"):
            count_me += 1
            print("Player gets 1 point\n")
    if (choice == "Water"):
        if (s == "G"):
            count_pc += 1
            print("PC gets 1 point\n")
        elif (s == "S"):
            count_me += 1
            print("Player gets 1 point\n")
    if (choice == "Gun"):
        if (s == "S"):
            count_pc += 1
            print("PC gets 1 point\n")
        elif (s == "W"):
            count_me += 1
            print("Player gets 1 point\n")
    count -= 1

if(count_pc > count_me):
    print("PC Win\n")
elif(count_pc < count_me):
    print("Player Win\n")
else:
    print("Match Drawn\n")