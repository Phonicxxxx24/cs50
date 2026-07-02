import csv
with open("dataset.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# testing line