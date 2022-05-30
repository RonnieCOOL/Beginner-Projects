import random

lst = ["Stone", "Paper", "Scissor"]

count_me = 0
count_pc = 0
count = 10

while(count != 0):
    choice = random.choice(lst)
    s = str(input("Type 'S' for Stone, 'P' for Paper and 's' for Scissor : "))

    if(choice == "Stone"):
        if(s == "s"):
            count_pc += 1
            print("PC gets 1 point\n")
        elif (s == "P"):
            count_me += 1
            print("Player gets 1 point\n")
    if (choice == "Paper"):
        if (s == "S"):
            count_pc += 1
            print("PC gets 1 point\n")
        elif (s == "s"):
            count_me += 1
            print("Player gets 1 point\n")
    if (choice == "Scissor"):
        if (s == "P"):
            count_pc += 1
            print("PC gets 1 point\n")
        elif (s == "S"):
            count_me += 1
            print("Player gets 1 point\n")
    count -= 1

if(count_pc > count_me):
    print("PC Win\n")
elif(count_pc < count_me):
    print("Player Win\n")
else:
    print("Match Drawn\n")