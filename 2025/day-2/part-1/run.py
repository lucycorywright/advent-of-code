
def is_id_invalid(id):
    length = (len(str(id)))
    return False if length % 2 == 1 else (True if str(id)[:length//2] == str(id)[length//2:] else False)

def get_invalid_ids(range_start, range_end):
    return list(filter(is_id_invalid, range(range_start, range_end+1)))

with open('input.txt') as file:
    ranges = [range.split('-') for range in file.read().split(',')]
 
all_invalid = [get_invalid_ids(int(range[0]), int(range[1])) for range in ranges]
print(sum([id for invalid_list in all_invalid for id in invalid_list]))

