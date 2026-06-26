def main():
    t1 = convert()
    if (t1>= 7 and t1<=8 ):
        print("Breakfast time ")
    elif(t1>=12 and t1<= 13):
        print("Lunch time")
    elif(t1>=18 and t1<= 19):
        print("Dinner time")

def convert():
    time = input("Enter the time: ")
    x,y = time.split(":")
    x = int(x)
    y = int(y)
    t = x + (y/60)
    return t

if __name__ == "__main__":
    main()
