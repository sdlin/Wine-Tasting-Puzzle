# Not guaranteed optimal
# First makes a dictionary with people for the keys, and a list of their wines as the values
# And makes a dictioanry with wines as the keys, and a 2 element list, with the first element 
# a list of people who want the wine, and the second element a taken flag (0 or 1)
# This goes through all people, looking at the subset of their preferred wines that are 
# still available, and selects up to 3 wines, starting with the wine with the least 
# number of people that want it and can still buy wine

# File with data:
input_filename = 'data/person_wine_4.txt'

output_filename = 'data/solution_wine4_.txt'

import csv

people = dict() # key: person, value: [wine1, wine2, ...]
wines = dict() # key: wine, value: [[person1, person2, ...], taken_flag]

# Read file and populate people and wines dictionaries
with open(input_filename, 'rb') as csvfile:
	tsv_data = csv.reader(csvfile, delimiter='	')
	for row in tsv_data:
		person = row[0]
		wine = row[1]
		if person in people:
			people[person].append(wine)
		else:
			people[person] = [wine]
		if wine in wines:
			wines[wine][0].append(person)
		else:
			wines[wine] = [[], 0]
			wines[wine][0] = [person]

# Print Stats:
print 'Number of wines: ' + str(len(wines))
print '3x Number of people: ' + str(3*len(people))

# Solve:
num_wines_sold = 0
solution = dict() # key: person, value: [wines bought]
for person in people:
	avail_wines = [[],[]] #[[wines that aren't taken], [# of ppl wanting that wine]]
	for wine in people[person]:
		if wines[wine][1] == 0: # if not taken
			avail_wines[0].append(wine)
			num_potential_buyers = 0
			for potential_buyer in wines[wine][0]:
				if potential_buyer in solution:
					if len(solution[potential_buyer]) <= 3:
						num_potential_buyers += 1
				else:
					num_potential_buyers += 1
			avail_wines[1].append(num_potential_buyers)
	for i in xrange(min([3,len(avail_wines[0])])): # choose up to 3 wines
		if len(avail_wines[0]) > 0:
			min_idx = avail_wines[1].index(min(avail_wines[1]))
			wine = avail_wines[0][min_idx] # wine with least # of ppl wanting it
			if person in solution:
				solution[person].append(wine)
			else:
				solution[person] = [wine]
			wines[wine][1] = 1 # mark wine as taken
			num_wines_sold += 1
			avail_wines[0].pop(min_idx)
			avail_wines[1].pop(min_idx)

# Print solution:
print str(num_wines_sold)
'''
for person in solution:
	for wine in solution[person]:
		print person + '	' + wine
'''

# Save solution:
with open(output_filename, 'wb') as csvfile:
	tsv_out = csv.writer(csvfile, delimiter='	')
	tsv_out.writerow([str(num_wines_sold)])
	for person in solution:
		for wine in solution[person]:
			tsv_out.writerow([person, wine])

# Check solution
print 'now lets check the solution...'
duplicates = 0
wines_chosen = dict()
max_person = ''
max_buys = 0
for sol_key in solution:
	for w in solution[sol_key]:
		if w in wines_chosen:
			duplicates += 1
		else:
			wines_chosen[w] = 0
	if len(solution[sol_key]) > max_buys:
		max_buys = len(solution[sol_key])
		max_person = sol_key
print 'duplicates: ' + str(duplicates)
print 'max buys: ' + str(max_buys)
print 'by: ' + sol_key