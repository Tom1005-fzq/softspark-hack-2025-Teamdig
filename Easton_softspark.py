import random


def play_game():
    target = random.randint(1, 100)
    attempts = 0

    print("I already choosed a number! Come and Guess!")

    while True:
        guess = int(input("Please enter your guess："))
        attempts += 1

        if guess < target:
            print("Too Low！")
        elif guess > target:
            print("Too high！")
        else:
            print(f"Congratulation! The correct is {target}")
            break

    if attempts <= 5:
        print(f"guess {attempts} times ，Excellent！")
    elif attempts <= 8:
        print(f"guess {attempts} times ，Good.")
    else:
        print(f"guess {attempts} times ，Need more practice...")


if __name__ == "__main__":
    play_game()