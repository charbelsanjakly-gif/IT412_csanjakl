# Problem 1 - low level open() version
# read the dinners file, tag each dinner with the day of the week, write it out as csv

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# read the 7 dinners in
infile = open("dinners.txt")
lines = infile.readlines()
infile.close()

# write dinner,day out to a new file
outfile = open("dinners_open_output.csv", "w")
for dinner, day in zip(lines, days):
    outfile.write(dinner.strip() + "," + day + "\n")
outfile.close()

print("done - wrote dinners_open_output.csv")
