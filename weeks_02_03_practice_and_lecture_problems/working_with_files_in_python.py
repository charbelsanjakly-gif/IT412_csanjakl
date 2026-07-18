# Demo - Working with Files in Python
# example code from the "Working with Files in Python" demo video (open() style)

# the video started on a .csv file using open()
f = open("sample.csv")
lines = f.readlines()
f.close()

# split each row on the comma
for line in lines:
    parts = line.strip().split(",")
    print(parts)

# reading a whole file at once
f = open("sample.csv")
contents = f.read()
f.close()
print(contents)

# reading line by line with a with-block (auto closes the file)
with open("sample.csv") as f:
    for line in f:
        print(line.strip())

# writing to a file - "w" makes a fresh file, "a" appends to the end
with open("notes.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")

with open("notes.txt", "a") as f:
    f.write("added later\n")

# read it back
with open("notes.txt") as f:
    print(f.read())
