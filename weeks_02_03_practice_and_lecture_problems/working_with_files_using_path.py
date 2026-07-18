# Demo - Working with Files Using Path
# example code from the "Working with Files Using Path" demo video

from pathlib import Path

# point Path at a file
p = Path("greeting.txt")

# write_text() creates/overwrites the file in one shot
p.write_text("hello from pathlib\n")

# read_text() reads the whole thing back
print(p.read_text())

# check if a file is there before touching it
if p.exists():
    print("greeting.txt exists")

# splitlines() is handy for looping over the contents
for line in p.read_text().splitlines():
    print(line)

# Path makes building file paths clean - no manual slashes
folder = Path("data")
folder.mkdir(exist_ok=True)
child = folder / "info.txt"
child.write_text("stored in a subfolder\n")
print(child.read_text())
