import random

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

chosen_number = random.choice(numbers)

print("Welcome to the number guessing game!")
print("A number has been chosen randomly from the list.")
print("Try to guess the chosen number but remember the number will be from the following list: 10,20, 30, 40, 50, 60, 70, 80, 90, or 100.")

while True:
    
    guess = int(input("Enter your guess: "))

    if guess == chosen_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > chosen_number:
        print("Sorry, the number you guessed is too high. Try again.")
    else:
        print("Sorry, the number you guessed is too low. Try again.")