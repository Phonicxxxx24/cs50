import sys
import csv
from tabulate import tabulate
if not len (sys.argv) == 2:
    sys.exit("inavlid number of Arguments")
if not sys.argv[1].endswith("csv"):
    sys.exit
try:
    with open(sys.argv[1]) as f:
        menu = csv.reader(f)
        print(tabulate(menu, headers=("firstrow"), tablefmt="grid"))
except FileNotFoundError:
    sys.exit


