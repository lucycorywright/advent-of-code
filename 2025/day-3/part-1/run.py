import numpy as np
from textwrap import wrap

def find_max_batteries(battery_line):
    batteries = wrap(battery_line, 1)
    
    index_max = np.argmax([int(battery) for battery in batteries[:-1]])
    index_next_max = np.argmax([int(battery) for battery in batteries[index_max+1:]]) + index_max + 1
    
    return int(str(batteries[index_max])+str(batteries[index_next_max]))

with open('input.txt') as file:
    battery_rows = [line.rstrip() for line in file]

test_list = ('987654321111111', '811111111111119', '234234234234278', '818181911112111') 
    
print(sum([find_max_batteries(battery_line) for battery_line in test_list]))
print(sum([find_max_batteries(battery_line) for battery_line in battery_rows]))