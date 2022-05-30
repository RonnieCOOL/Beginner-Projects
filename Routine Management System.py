# Health Management System
# 3 clients - Ankan, Joy and Ashish
# taking note of what one does with time stamp
# format [time] chicken, roti.. etc etc

def gettime():
    import datetime
    return datetime.datetime.now()

def take(k):
    if(k==1):
        c = int(input("Enter 1 for Exercise and 2 for Food : "))

        if(c == 1):
            value = input("Type Here\n")
            with open("Ankan-Exercise.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully Written")
        elif(c == 2):
            value = input("Type Here\n")
            with open("Ankan-Diet.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Successfully Written")

    elif(k == 2):
        c = int(input("Enter 1 for Exercise and 2 for Food : "))

        if (c == 1):
            value = input("Type Here\n")
            with open("Joy-Exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        elif (c == 2):
            value = input("Type Here\n")
            with open("Joy-Diet.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Successfully Written")


    elif(k == 3):
        c = int(input("Enter 1 for Exercise and 2 for Food : "))

        if (c == 1):
            value = input("Type Here\n")
            with open("Ashish-Exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully Written")
        elif (c == 2):
            value = input("Type Here\n")
            with open("Ashish-Diet.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Successfully Written")


def retrieve(k):
    if (k==1):
        c = int(input("Enter 1 for Exercise and 2 for Food : "))
        if(c == 1):
            with open("Ankan-Exercise.txt") as op:
                for i in op:
                    print(i, end = "")

        elif(c == 2):
            with open("Ankan-Diet.txt") as op:
                for i in op:
                    print(i, end="")


    elif (k == 2):
        c = int(input("Enter 1 for Exercise and 2 for Food : "))
        if(c == 1):
            with open("Joy-Exercise.txt") as op:
                for i in op:
                    print(i, end = "")

        elif(c == 2):
            with open("Joy-Diet.txt") as op:
                for i in op:
                    print(i, end="")

    elif (k == 3):
        c = int(input("Enter 1 for Exercise and 2 for Food : "))
        if(c == 1):
            with open("Ashish-Exercise.txt") as op:
                for i in op:
                    print(i, end = "")

        elif(c == 2):
            with open("Ashish-Diet.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input!")

print("HEALTH MANAGEMENT SYSTEM")
a = int(input("Press '1' for 'Log' and '2' for 'Retrieve : '"))

if(a == 1):
    b = int(input("Press '1' for 'Ankan', '2' for 'Joy', '3' for 'Ashish'"))
    take(b)
else:
    b = int(input("Press '1' for 'Ankan', '2' for 'Joy', '3' for 'Ashish'"))
    retrieve(b)