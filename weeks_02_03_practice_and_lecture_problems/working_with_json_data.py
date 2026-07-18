# Demo - Working with JSON Data
# example code from the "Working with JSON Data" demo video

import json

# some data to work with
numbers = [2, 3, 5, 7, 11, 13]

# dumps() turns python data into a json string, loads() turns it back
text = json.dumps(numbers)
print(text)
back = json.loads(text)
print(back)

# dump() writes straight to a file, load() reads straight from one
with open("numbers.json", "w") as f:
    json.dump(numbers, f)

with open("numbers.json") as f:
    stored = json.load(f)
print(stored)

# json handles dictionaries too
user = {"name": "charbel", "shows": ["The Office", "Breaking Bad"]}
with open("user.json", "w") as f:
    json.dump(user, f)

with open("user.json") as f:
    loaded = json.load(f)
print(loaded["name"])
print(loaded["shows"])
