import random
answer = random.randint(1,100)
guesses = 0
while True:
    choice = input("guess a number(1-100): ")
    guesses += 1
    if choice.isdigit():
        choice  = int(choice)
        if choice < 1 or choice > 100:
            print("out of range")
        elif choice < answer:
            print("too low")
        elif choice > answer:
            print("too high")
        else:
            print("correct")
            print(f'guesses = {guesses}')
            again = input("play again(y/n): ").lower()
            if again != "y":
                break
    else:
        print("invalid")
print("bye")