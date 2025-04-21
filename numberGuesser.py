import random 

actual = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("\nPlease select the difficulty level:")
print("1. Easy (10 guesses)")
print("2. Medium (5 guesses)")
print("3. Hard (3 guesses)")

diff = input("\nEnter your choice: ")

def choice():
    for x in range(guess):
        num = input("Enter your choice: ")
        if num.isnumeric():
            num = int(num)
        else:
            print("The input is not valid. Please try again.") 
            break
        
        
        if num < actual:
            print(f"Incorrect! The number is greater than {num}.\n")
        elif num > actual:
            print(f"Incorrect! The number is less than {num}.\n")
        elif num == actual:
            print(f"Congratulations! You guessed the number in {x} attempts.")
            break
            
        if x == guess - 1:
            print(f"You ran out of guesses. The number was {actual}. Thanks for playing!")
            break

if diff == "1":
    guess = 10
    print("You selected Easy.\n")
    choice()
    
    
elif diff == "2":
    guess = 5
    print("You selected Medium.\n")
    choice()
    
elif diff == "3":
    guess = 3
    print("You selected Hard.\n")
    choice()
    
else:
    print("Input error! Please try again.")



