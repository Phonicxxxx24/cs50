# The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

# Hints
# Rather than use a conditional with 20 Boolean expressions, one for each fruit, better to use a dict to associate a fruit with its calories!
# If k is a str and d is a dict, you can check whether k is a key in d with code like:
# if k in d:
#     ...
# Take care to output the fruit’s calories, not calories from fat!

def main():
    Item = input("Item: ")
    Item = Item.lower()
    calorie_info(Item)


def calorie_info(k):
    calories_dict = {
        "apple": 130,
        "avocado": 50, 
        "banana" : 110,
        "grapes" : 90,
        "lemon" : 15,
        "kiwifruit" : 90,
        "orange" : 80,
        "grapefruit" : 60,
        "lime":20,
        "Pear": 100,
        "pineapple": 50,
        "plums": 70, 
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 50

    }
    
    if k in calories_dict:
        print(f"caolries: {calories_dict[k]}")
main()