#Question: How do violent conflicts between the government and citizens compare for the year 1989 (after the fall of communism) and the year 1999 (after the fall of the mafia govt)
#from the dataset, select only those entries for BUL and save them in another dataset (csv) and work with that
#select entries for the year 1989 an 1999

import json
import csv 

conflicts_bul = []

with open ('conflict_data_full_lined.json', encoding='utf-8-sig') as file:
    conflicts = json.load(file)
    for conflict in conflicts:
        if "Bulgaria" in conflict['country']:
            # Add value to the new list
            conflicts_bul.append()

print(conflicts_bul)