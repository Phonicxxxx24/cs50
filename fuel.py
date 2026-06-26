
def fuel():
    while True:
        try:
            values = input("Fraction: ") 
            values = values.split("/")  
            x = int(values[0])
            y = int(values[1])
            percentage = (x)/(y)*100    
            percentage = round(percentage)
            if percentage < 0:
                continue
            elif x <0 or y<0:
                continue
            elif x>y:
                continue
            elif percentage <= 1:
                print("E")
            elif percentage >= 99 :
                print("F")
            else:
                print(f"{percentage}%")
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

fuel()
    
