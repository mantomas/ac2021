def parse_data(file_name):
    with open(file_name, "r") as f:
        numbers = [int(i) for i in f.read().split(',')]
        return numbers


# PART 1
def part_one(data):
    start = min(data)
    stop = max(data)
    while True:
        possition = int((start + stop) / 2)
        cost = cost_part_one(possition, data)
        previous = cost_part_one(possition - 1, data)
        next = cost_part_one(possition + 1, data)
        if cost == min([previous, cost, next]):
            return cost
        elif previous < cost:
            stop = possition
        else:
            start = possition


def cost_part_one(possition, data):
    fuel = 0
    for i in data:
        fuel += abs(possition - i)
    return fuel


# PART 2
def part_two(data):
    start = min(data)
    stop = max(data)
    while True:
        possition = int((start + stop) / 2)
        cost = cost_part_two(possition, data)
        previous = cost_part_two(possition - 1, data)
        next = cost_part_two(possition + 1, data)
        if cost == min([previous, cost, next]):
            return cost
        elif previous < cost:
            stop = possition
        else:
            start = possition


def cost_part_two(possition, data):
    cost = 0
    for i in data:
        distance = abs(i - possition)
        single_cost = 0
        for j in range(distance + 1):
            single_cost += j
        cost += single_cost
    return cost


def main(file_name):
    data = parse_data(file_name)
    least_fuel_part_one = part_one(data)
    least_fuel_part_two = part_two(data)
    return least_fuel_part_one, least_fuel_part_two


if __name__ == '__main__':
    part_1, part_2 = main("day_7_in.txt")
    print(f"Part one: {part_1}")
    print(f"Part two: {part_2}")
