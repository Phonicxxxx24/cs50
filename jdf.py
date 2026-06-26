x = 2
y = 3
z = x+y
i =0

while i<3:   
    ans = (int(input(f"{x} + {y} = "))) 

    try:
        if ans == z:
            print("correct")
            break
        elif i == 3:
            break
        else:
            print("eee")        
    except:
        pass
    i = i+1
print(f"answer is {z}")