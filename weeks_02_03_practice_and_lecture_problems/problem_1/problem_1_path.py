# Problem 1 - Path version
# same idea as the open() version but using pathlib, and a different output file

from pathlib import Path

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# read the whole file and split it into lines
lines = Path("dinners.txt").read_text().splitlines()

# build up the new csv lines
out = []
for dinner, day in zip(lines, days):
    out.append(dinner.strip() + "," + day)

# write them all to a new file
Path("dinners_path_output.csv").write_text("\n".join(out) + "\n")

print("done - wrote dinners_path_output.csv")
