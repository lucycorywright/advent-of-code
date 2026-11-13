import functools

initial_dial_point = 50
total_clicks = 0

def apply_rotation(current_point, rotation):
    global total_clicks

    direction = rotation[0]
    amount = int(rotation[1:])

    if direction == 'R':
        total_clicks += (current_point + amount) // 100
        return (current_point + amount) % 100

    if current_point == 0:
        total_clicks += amount // 100
    else:
        total_clicks += (amount + 100 - current_point) // 100
    return (current_point - amount) % 100

with open('input.txt') as file:
    rotations = [line.rstrip() for line in file]
    
test_list = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
    
rotation_applied_points = functools.reduce(apply_rotation, rotations, initial_dial_point)
print(total_clicks)
