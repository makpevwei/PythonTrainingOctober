import random

print("Welcome to the Guess a Number Game!")
print("-" * 30)

secret_number = random.randint(1, 30)
attempt = 0

while True:
    try:
        guess = int(input("Guess a number from 1 to 30: "))
        attempt += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number correctly in {attempt} attempt(s)." )
            again = input("Do you want to play again: (yes/no): ").strip().lower()
            if again in ["yes", "y", "YES"]:
                secret_number = random.randint(1, 30)
                attempt = 0
                continue
            else:
                print("Thanks for playing. Goodbye...")
                break
        elif guess < secret_number:
            print("Low! Try going higher.")
            
        else:
            print("High! Try going lower.")
            
    except ValueError:
        print("Invalid input. Please enter a whole number.")