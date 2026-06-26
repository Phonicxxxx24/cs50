months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("date: ")
    if "/" in date :
        date = date.split("/")
        print(f"{date[2]:02}-{int(date[0]):02}-{int(date[1]):02}")
        break



    elif "," in date:
            date = date.split(",")
            f_part = date[0].split(" ")
            month = f_part[0].title()
            dates = f_part[1]
            if month in months:
                print(f"{int(date[1])}-{int(months.index(month))+1:02}-{int(dates):02}")
                break
