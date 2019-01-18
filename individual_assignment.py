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
            #pass #do nothing
            #select all entries for Afghanistan for 1998 and for 
            if conflict['year'] == 1998 or conflict['year'] == 2004:
                #print(f'{conflict["year"]} is of type {type(conflict["year"])}')
                conflicts_afg.append(conflict)

#print(json.dumps(conflicts_afg, indent=4)) #pretty print it in the terminal
#print(len(conflicts_afg)) #how many dictionaries in the list

#make it into a csv file
headers = ['Conflict.Name', 'Type.of.violence', 'Year', 'Long', 'Lat', 'Side.A', 'Side.B', 'Deaths.A', 'Deaths.B']

with open('afghanistan.csv', 'w', newline='') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(headers)
    for conflict in conflicts_afg:
        filewriter.writerow([conflict['conflict_name'], conflict['type_of_violence'], conflict['year'], conflict['longitude'], conflict['latitude'], conflict['side_a'], conflict['side_b'], conflict['deaths_a'], conflict['deaths_b']])

