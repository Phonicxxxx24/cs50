import sys
import csv
from tabulate import tabulate
# if not len (sys.argv) == 3:
#     sys.exit("inavlid number of Arguments")
# if not sys.argv[1].endswith("csv") and sys.argv[2].endswith(".csv"):
#     sys.exit

try:
    with open(sys.argv[1]) as f1, open(sys.argv[2], "w", newline="") as f2:
        reader = csv.DictReader(f1)
        writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            full_name = row["name"]
            parts = full_name.split(", ")
            last = parts[0]
            first = parts[1]
            writer.writerow({"first":first, "last": last, "house":row["house"]})

        # name = csv.DictReader(f)
        # for names in name:

        #     with open(sys.argv[2], "w", newline="") as f:
        #         fieldnames = ["first", "last", "house"]
        #         writer = csv.DictWriter(f, fieldnames=fieldnames)
        #         writer.writeheader()
        #         writer.writerow({"first": first, "last": last, "house": name["house"]})
            
except FileNotFoundError:
    sys.exit
