import numpy as np
from textwrap import wrap

def find_max_batteries(battery_line):

    indexes = [int(n) for n in np.zeros(12)]
    
    for i in range(0, 12):
        if i == 0 :
            indexes[i] = int(np.argmax([int(battery) for battery in battery_line[:-11]]))
        else :
            start = indexes[i-1]+1
            end = len(battery_line)-(11-i)
            indexes[i] = int(np.argmax([int(battery) for battery in battery_line[start:end]]) + indexes[i-1] + 1)
    
    max_value = ''
    for i in indexes:
        max_value = max_value + battery_line[i]
    
    return int(max_value)

with open('input.txt') as file:
    battery_rows = [line.rstrip() for line in file]

test_list = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
    
print(sum([find_max_batteries(battery_line) for battery_line in test_list]))
print(sum([find_max_batteries(battery_line) for battery_line in battery_rows]))