from datetime import date
import sys
import inflect
p = inflect.engine()

# get input, call other functions, print result
def main():
    try:
        dob = input("Enter Date of Birth: ")
        birth = date.fromisoformat(dob)
    except:
        sys.exit("Incorrect format \nplease enter DOB in YYYY-MM-DD format")
    today = date.today()
    getting_minutes = get_minutes(birth, today)
    print(minutes_to_words(getting_minutes))

# calculate and return minutes
def get_minutes(birth, today):

    delta = (today - birth)
    minutes = delta.days * 24 * 60
    return minutes

# convert to English words and return...
def minutes_to_words(minutes):
    return (f"{p.number_to_words(minutes).replace(" and","")} minutes")

if __name__ == "__main__":
    main()