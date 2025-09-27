import random

def play_game():

    target = random.randint(1, 100)
    attempts = 0

    print('I already choosed a number! Come and Guess!')

    while True:
        guess = int(input("Enter the number you guessed:"))
        attempts += 1

        if guess < target:
            print("Too Low")
        elif guess > target:
            print("Too High")
        else:
            print(f"Congratulation! The correct is {target}")
            break

if __name__ == "__main__":
    play_game()
