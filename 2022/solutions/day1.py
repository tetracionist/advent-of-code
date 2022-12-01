# first read the input and get the data into python
# this could be generic
import os
input_directory = f"{os.path.dirname(os.path.dirname(__file__))}\inputs"
day1_data = f"{input_directory}\day1.txt"

f = open(day1_data, "r")
data = f.read()

# Used this to find what represents an empty line
# print(repr(data))

elf_view = []

elves = data.split('\n\n')
for elf in elves:
    elf_view.append(sum([int(i) for i in elf.split('\n')]))

# greatest number of calories that an elf is carrying 
print(max(elf_view))

# sort the data to get the top three elves
# Then get the indexes
top_3_elves = sorted(elf_view, reverse=True)[:3]

# the sum of calories that the top three elves are carrying
print(sum(top_3_elves))