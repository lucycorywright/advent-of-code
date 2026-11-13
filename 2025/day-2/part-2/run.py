from textwrap import wrap

def get_factors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors

def is_id_invalid(id):
    factors = get_factors(len(str(id)))
    valid = False
    for factor in factors:
        chunks = wrap(str(id), width=factor)
        if chunks.count(chunks[0]) == len(chunks) :
            valid = True
    return valid

def get_invalid_ids(range_start, range_end):
    return list(filter(is_id_invalid, range(range_start, range_end+1)))

with open('input.txt') as file:
    ranges = [range.split('-') for range in file.read().split(',')]
 
all_invalid = [get_invalid_ids(int(range[0]), int(range[1])) for range in ranges]
print(sum([id for invalid_list in all_invalid for id in invalid_list]))

