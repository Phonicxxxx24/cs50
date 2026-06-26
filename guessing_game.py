import random

def game():
        # first loop: get valid level
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    # generate number once
    number = random.randint(1, level)

    # second loop: keep guessing
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0 :
                if guess < number:
                    print("Too small")
                
                elif guess > number:
                    print("Too big")
                
                elif number == guess:
                    print("Just Right")
                    break
                # compare and print
        except ValueError:
            pass

game()
