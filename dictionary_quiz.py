import pandas as pd
sports = [
    { 
        "name": "Peach",
        "items": ["green shell", "banana", "green shell"],
        "finish" : 3
    },
    {
        "name": "Browser",
        "items": ["green shell"],
        "finish" : 1
    },
    {
        "name": None,
        "items": ["mush room"],
        "finish" : 2
    },
    {
        "name": "Toad",
        "items": ["green shell", "mush room"],
        "finish" : 1
    }
]
print(sports)
print(f"The lenght of the list is {len(sports)}")

## iterate over
a = 1
for item in sports:
    print(f"Item No : {a}")
    print(item)
    a += 1

print("\n")
print("\n")

#check names for finish 1
winning_items = []
for item in sports:
    # print(item["name"])
    if item["finish"] == 1:
        print(f" The name of the runner is {item['name']} and used {item['items']}")
        for material in item['items']:
            if material in winning_items:
                pass
            else:
                winning_items.append(material)

print(f"Materials used by the winners are {winning_items}")

print("\n")
print("\n")

## record number of times item is used and place in a dictionary
winner_material_used = {}
for item in sports:
    # print(item["name"])
    if item["finish"] == 1:
        print(f" The name of the runner is {item['name']} and used {item['items']}")
        for material in item['items']:
            if material not in winner_material_used:
                winner_material_used[material] = 1 
            else:
                winner_material_used[material] += 1
            # count_number += 1

print(winner_material_used)