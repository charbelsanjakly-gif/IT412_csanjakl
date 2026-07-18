# Problem 2
# keep asking the user for hobbies and save each one to a file on its own line

f = open("hobbies_list.txt", "w")

while True:
    hobby = input("Enter a hobby (type 'quit' to stop): ")
    if hobby == "quit":
        break
    f.write(hobby + " is a hobby I like.\n")

f.close()
print("saved to hobbies_list.txt")
