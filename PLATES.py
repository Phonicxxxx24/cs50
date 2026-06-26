import string
def main():
    plate = input("plate: ")
    if validation(plate):
        print("Vallid")
    else:
        print("Invalid")

def validation(s):
    
    # checking length and first two are alphabets

    if len(s)<2 or len(s)>6:
        return False
    if not (s[0].isalpha() and s[1].isalpha() ):
        return False
    
    # checking integers in between or at last
    
    digit_seen = False
    for i in s:
        if i.isdigit() and not digit_seen and i == "0":
            return False
        if (i.isdigit()):
            digit_seen = True
        if (i.isalpha() and digit_seen ):
            return False
        if i.isdigit():
            digit_seen = True
        
        # Checking space and punctuation
        if (i.isspace()):
            return False
        if (i in string.punctuation):
            return False
    return True
main()