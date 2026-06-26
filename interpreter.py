expression = input('Expression: ')
x,y,z = expression.split(' ') 
x = int(x)
z = int(z)
if (y == "+"):
    c = x + z  
    print(f"{c:.1f}")
elif (y == "-"):
    c = x - z  
    print(f"{c:.1f}")
elif (y == "*"):
    c = x * z  
    print(f"{c:.1f}")
elif (y == "/"):
    c = x / z  
    print(f"{c:.1f}")