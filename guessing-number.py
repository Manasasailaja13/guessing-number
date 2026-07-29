from getpass import getpass

print("===================================")
print("   NUMBER GUESSING GAME")
print("===================================")

print("Select Difficulty Level")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    print("\nEasy Level")
    print("Secret number should be between 1 and 10")
    attempts = 5

elif choice == "2":
    print("\nMedium Level")
    print("Secret number should be between 1 and 50")
    attempts = 7

elif choice == "3":
    print("\nHard Level")
    print("Secret number should be between 1 and 100")
    attempts = 10

else:
    print("Invalid Choice!")
    exit()

number = (getpass("\nPlayer 1: Enter the secret number: "))

print("\n" * 30)   # Clears the screen by pushing the secret number out of view

print("Player 2, start guessing!")

while attempts > 0:

    guess = (input("Enter your guess: "))

    if guess == number:
        print("\n🎉 Congratulations! You guessed the correct number.")
        break

    elif guess < number:
        print("Too Low!")

    else:
        print("Too High!")

    attempts = attempts - 1
    print("Attempts Left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The secret number was:", number)

print("\nThank You For Playing!")