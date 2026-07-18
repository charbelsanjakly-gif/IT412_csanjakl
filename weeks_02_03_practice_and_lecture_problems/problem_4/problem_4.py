# Problem 4
# load favorite shows from a json file, or build the list if there's nothing saved yet

import json
import os

def get_shows():
    # loop and collect shows, each one stored as its own dictionary
    shows = []
    while True:
        name = input("Enter a favorite TV show (type 'done' to finish): ")
        if name == "done":
            break
        shows.append({"show": name})
    return shows

filename = "favorite_shows.json"

# see if we already have saved data
data = None
if os.path.exists(filename):
    contents = open(filename).read()
    if contents.strip() != "":
        data = json.loads(contents)

if data:
    # file has data - show it, then ask if they want to change it
    print("Here are your saved shows:")
    for item in data:
        print("-", item["show"])

    answer = input("Would you like to modify your list? (yes/no): ")
    if answer == "yes":
        shows = get_shows()
        open(filename, "w").write(json.dumps(shows))
        print("list updated")
else:
    # no file or nothing in it - build the list from scratch
    shows = get_shows()
    open(filename, "w").write(json.dumps(shows))
    print("saved your shows")
