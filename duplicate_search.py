#!/usr/bin/env python3

import csv
from typing import Dict
from soundex import Soundex

soundex = Soundex()

trees = []
with open('tree_list.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        trees.append(row)

names: Dict[str, Dict[int, str]] = {}
botanical_names: Dict[str, Dict[int, str]] = {}

for tree in trees:
    id = tree['ID']
    name = tree['Name'].lower()
    name_ex = soundex.soundex(name)
    botanical_name = tree['Botanical name'].lower()
    botanical_name_ex = soundex.soundex(botanical_name)
    
    if name_ex not in names.keys():
        names[name_ex] = {}
    if botanical_name_ex not in botanical_names.keys():
        botanical_names[botanical_name_ex] = {}
    
    if id not in names[name_ex].keys():
        names[name_ex][id] = name
    if id not in botanical_names[botanical_name_ex].keys():
        botanical_names[botanical_name_ex][id] = botanical_name
    
print([name for name in names.values() if len(name.keys()) > 1])

for botanical_name in [botanical_name for botanical_name in botanical_names.values() if len(botanical_name.keys()) > 1]:
    print(f'- {list(botanical_name.values())[0]} : {", ".join(botanical_name.keys())}')
