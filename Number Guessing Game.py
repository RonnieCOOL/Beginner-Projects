# Take a number and take guesses from the user. If the guess is correct, print Hurray! You guessed the answer right!

n1 = 18
number_of_guesses = 1 
print("RULE:- You are given 9 guesses to guess my number (between 1 to 20), If you fail, I win! <3\n")
print("So, Ready to start?  Yes/No?")
yn = input()

if yn == "Yes":
    while(number_of_guesses <=9):
         n2 = int(input("Guess the Number! \n"))
         if n2 > n1:
            print("My number is Lesser than your number.")
         if n2 < n1:
            print("My number is Greater than your number.")
         if n2 == n1:
            print("You Won!")
            print(number_of_guesses, "guesses taken")
            break
         print(9 - number_of_guesses, "guesses left.\n")
         number_of_guesses = number_of_guesses + 1
    if(number_of_guesses>9):
        print("Game Over!")
if yn == "No":
    print("You are a Loser. \nI WON!")
