import os, string
day = os.path.basename(__file__).split('.')[0]
read_file = f"{os.path.dirname(os.path.dirname(__file__))}\inputs\{day}.txt"

f = open(read_file, "r")
data = f.read()
f.close()

test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

# split lines into a oython list does seem to be a generic thing with these puzzles so far
# The data contains pairs separated by a new line so I'm going to tidy this up to make each pair exist inside a tuple within a list
data_list = [(i.split(',')[0], i.split(',')[1]) for i in data.splitlines()] 

counter_part1 = 0
counter_part2 = 0

# create two arrays to compare against
# and see if the minimum or maximum are in the list
for i in data_list:
    a = i[0].split('-') 
    b = i[1].split('-')

    arr_1 = [j for j in range(int(a[0]), int(a[1])+1, 1)]   
    arr_2 = [j for j in range(int(b[0]), int(b[1])+1, 1)]

    counter_part1 = counter_part1 + 1 if (max(arr_1) in arr_2 and min(arr_1) in arr_2) or (max(arr_2) in arr_1 and min(arr_2) in arr_1) else counter_part1
    counter_part2 = counter_part2 + 1 if min(arr_1) in arr_2 or min(arr_2) in arr_1 or max(arr_1) in arr_2 or max(arr_2) in arr_1 else counter_part2

print(counter_part1)
print(counter_part2)