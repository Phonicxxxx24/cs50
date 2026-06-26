import inflect

def main():
    # list that stores all names
    name_list = []
    # takes all names as a input
    while True:
        try:
            names = input("Name: ") 
            name_list.append(names)
        except EOFError:
            break
    print(bye(name_list))
    

def bye(x):
    p = inflect.engine()
    all_names = p.join(x)
    return f"Adieu, adieu, to {all_names}"

main()