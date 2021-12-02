with open("day_2_in.txt", "r") as f:
    planned_course = [
        (direction.split()[0], int(direction.split()[1])) for direction in f.readlines()
    ]

# part 1

depth = 0
distance = 0

for command, value in planned_course:
    if command == "forward":
        distance += value
    elif command == "down":
        depth += value
    else:
        depth -= value
        if depth < 0: # can submarine fly?
            depth = 0

print(distance * depth)

# part 2

depth2 = 0
distance2 = 0
aim = 0

for command, value in planned_course:
    if command == "forward":
        distance2 += value
        if aim > 0:
            depth2 += value * aim
        elif aim < 0:
            depth2 -= value * abs(aim)
            if depth2 < 0: # no, submarines canot fly
                depth2 = 0
    elif command == "down":
        aim += value
    else:
        aim -= value


print(depth2 * distance2)
