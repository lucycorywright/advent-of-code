import functools

initial_dial_point = 50
with open('output.txt', 'w') as file:
    file.write('')

def apply_rotation(current_point, rotation):
    direction = rotation[0]
    amount = int(rotation[1:])
    updated_point = ((current_point + amount) if direction == "R" else (current_point - amount)) % 100
    with open('output.txt', 'a') as file:
        file.write(str(updated_point)+'\n')
    return updated_point

with open('input.txt') as file:
    rotations = [line.rstrip() for line in file]

rotation_applied_points = functools.reduce(apply_rotation, rotations, initial_dial_point)
    
with open('output.txt') as file:
    password = [int(line.rstrip()) for line in file].count(0)
    
print(password)