import sys
if not len(sys.argv) == 2:
    sys.exit("inavlid number of Arguments")

if not sys.argv[1].endswith("py"):
    print("not a python file")
try:
    with open(sys.argv[1]) as f:
        line = 0
        for rows in f:
            stripped = rows.strip()
            if stripped == "" or rows.startswith("#"):
                continue
            line += 1
        print(line)
except FileNotFoundError:
    sys.exit("File not Found")    
