import random
def get_level():
    while True:
        try:
            level = int(input("Enter level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    low = 10 ** (level - 1) if level > 1 else 0
    high = 10 ** (level) - 1    
    return random.randint(low,high)

def calculation(level):
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z=x+y
        i = 0

        while i < 3:    
            ans = (int(input(f"{x} + {y} = ")))

            try:
                if ans == z:
                    print("correct")
                    score+=1
                    break
                elif i == 3:
                    break
                else:
                    print("eee")        
            except ValueError:
                    print("eee")            
            i = i+1
        else:
            print(f"Correct Answer is: {x} + {y} = {z}")


    print(f"Score: {score}/10")

level = get_level()
calculation(level)