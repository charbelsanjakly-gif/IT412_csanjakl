# Demo - CSV using Path instead of open()
# the "Working with Files in Python" video started with a .csv using open().
# this is that same csv code converted over to use Path.

from pathlib import Path

# open() version was: f = open("sample.csv"); lines = f.readlines(); f.close()
# Path version reads the whole file and splits it into lines
lines = Path("sample.csv").read_text().splitlines()

# split each row on the comma, same as before
for line in lines:
    parts = line.split(",")
    print(parts)
