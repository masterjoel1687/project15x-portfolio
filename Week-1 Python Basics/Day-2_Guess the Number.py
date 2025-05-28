import random   
numberof_guesses = 3
secret_number = random.randint(1, 10)  
print("Welcome to the Guess the Number game!")
print("You have", numberof_guesses, "guesses to find the secret number.")
guess = int(input("Guess the secret number (between 1 and 10): "))
if guess == secret_number:
    print("Congratulations! You guessed the secret number.")
else:
    print("Sorry, that's not the secret number. Try again!")
while numberof_guesses > 1 and guess != secret_number:
    numberof_guesses -= 1
    guess = int(input("You have " + str(numberof_guesses) + " guesses left. Guess again: "))
    if guess < 1 or guess > 10:
        print("Please guess a number between 1 and 10.")
    if guess < secret_number:
        print("Hint: The secret number is higher than your guess.")
    else:
        print("Hint: The secret number is lower than your guess.")