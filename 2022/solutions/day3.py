import os, string
day = os.path.basename(__file__).split('.')[0]
read_file = f"{os.path.dirname(os.path.dirname(__file__))}\inputs\{day}.txt"

f = open(read_file, "r")
data = f.read()
f.close()

# test data 
test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
#print(test_data)

#print(data)

# make a lookup so taht we can get a score for each item
priotity = [[chr(ord('a') + i), i+1] for i in range(26)] + [[chr(ord('A') + i), i+27] for i in range(26)]
priority_dict = {}

for i in priotity:
   priority_dict[i[0]] = i[1]

# the first half of the characters is the first compartment 
rucksack_list = []
score_list = []

for rucksack in data.splitlines():
    first_compartment = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]
    rucksack_list.append([first_compartment, second_compartment])

# for each rucksack, find the item type that appears in both compartments
for rucksack in rucksack_list:
    for item in rucksack[0]:
        if item in rucksack[1]:
            score_list.append(priority_dict[item])
            break

print(sum(score_list))

# part 2
# each three lines represents a group
#print(data.splitlines())

group_list = []
score_list_2 = []

for i in range(2, len(data.splitlines()), 3):
    group_list.append([data.splitlines()[i-2],data.splitlines()[i-1], data.splitlines()[i]])

# then find the item that appears in each rucksack within the group
for group in group_list:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            score_list_2.append(priority_dict[item])
            break

print(sum(score_list_2))