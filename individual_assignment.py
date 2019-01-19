#Question: How do violent conflicts between the government and citizens compare for the year 1998 (some peak there; what happened?) and the year 2004 (no peak; why? what happened?)
#from the dataset, select only those entries for AFG and save them in another dataset (csv) and work with that
#select entries for the year 1998 and 2004

import json
import csv 

conflicts_afg = []

with open ('conflict_data_full_lined.json', encoding='utf-8-sig') as file:
    conflicts = json.load(file)
    for conflict in conflicts:
        #select all entries for Afghanistan
        if "Afghanistan" in conflict['country']:
            #select all entries for Afghanistan for 1998 and for 2004:
            if conflict['year'] == 1998 or conflict['year'] == 2004:
                if 'Taleban' in conflict['side_b'] or 'UIFSA' in conflict['side_b']:
                    conflicts_afg.append(conflict)

#make it into a csv file
headers = ['Conflict.Name', 'Year', 'Long', 'Lat', 'Side.A', 'Side.B', 'Deaths.Civilians']

with open('afghanistan.csv', 'w', newline='') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(headers)
    for conflict in conflicts_afg:
        filewriter.writerow([conflict['conflict_name'], conflict['year'], conflict['longitude'], conflict['latitude'], conflict['side_a'], conflict['side_b'], conflict['deaths_civilians']])

