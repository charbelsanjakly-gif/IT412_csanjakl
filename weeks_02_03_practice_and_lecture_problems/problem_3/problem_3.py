# Problem 3
# same as problem 1 but wrapped so it just fails silently if a file isn't found

from pathlib import Path

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# open() version
try:
    infile = open("dinners.txt")
    lines = infile.readlines()
    infile.close()

    outfile = open("dinners_open_output.csv", "w")
    for dinner, day in zip(lines, days):
        outfile.write(dinner.strip() + "," + day + "\n")
    outfile.close()
except FileNotFoundError:
    pass

# Path version
try:
    lines = Path("dinners.txt").read_text().splitlines()
    out = []
    for dinner, day in zip(lines, days):
        out.append(dinner.strip() + "," + day)
    Path("dinners_path_output.csv").write_text("\n".join(out) + "\n")
except FileNotFoundError:
    pass
