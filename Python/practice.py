import random

tries = 3

while tries > 0:
    rand_num = random.randint(0, 5)
    guess = int(input("Guess a number between 0 and 10!"))
    if guess == rand_num:
        print("Yay! you won! now leave")
        break
    else:
        print("You are not really good at this are you?")
        print(f"The number was {rand_num}")
        # tries = tries - 1
        tries -= 1

if tries == 0:
    print("Congrats you lost!")
else:
    print("Success!")