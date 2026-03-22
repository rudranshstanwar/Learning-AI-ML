info = [
    ("Alice", "Math"),
    ("Bob",  "Science"),
    ("Alice",  "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

subjects = set()
print("Subjects are: ")
for i in info:
    subjects.add(i[1])
print(f"{subjects}\n\n")

names_english = []
print("Students enrolled in English are: ")
for i in info:
    if i[1] == "English":
        names_english.append(i[0])
print(f"{names_english}\n\n")

dict = {}
for i in info:
    if dict.get(i[0]) == None:
        dict.update({i[0]:set()})
        dict[i[0]].add(i[1])
    else:
        dict[i[0]].add(i[1])
print(dict)