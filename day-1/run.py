
initial_dial_point = 50

def apply_rotation(current_point, direction, amount):
    return ((current_point + amount) if direction == "R" else (current_point - amount)) % 100

