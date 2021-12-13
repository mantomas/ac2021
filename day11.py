def parse_data(file_name):
    with open(file_name, "r") as f:
        data = f.readlines()
        grid = [[int(dumbo) for dumbo in line.strip()] for line in data]
        return grid


# PART 1
def part_one(file_name, rounds):
    grid = parse_data(file_name)
    total_flashes = 0
    for _ in range(rounds):
        grid = flash(grid)
        total_flashes += count_flashes(grid)
    return total_flashes


def count_flashes(grid):
    flashes = 0
    for row, line in enumerate(grid):
        for col, dumbo in enumerate(line):
            if dumbo == 0:
                flashes += 1
    return flashes


def neighbours(width, heigt, x, y):
    raw_neighbours = [
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ]
    real_neighbours = []
    for i in raw_neighbours:
        if i[0] < 0 or i[1] < 0:
            continue
        if i[0] >= heigt or i[1] >= width:
            continue
        real_neighbours.append(i)
    return real_neighbours


def flash(grid):
    # limit borders
    width = len(grid[0])
    height = len(grid)
    # start next round
    for row, line in enumerate(grid):
        for col, dumbo in enumerate(line):
            grid[row][col] += 1
    # monitor which dumbo flashed
    dumbo_flashed = []
    # cycle grid until dombos flashed
    while True:
        dumbo_go = False
        for row, line in enumerate(grid):
            for col, dumbo in enumerate(line):
                if grid[row][col] > 9 and (row, col) not in dumbo_flashed:
                    dumbo_flashed.append((row, col))
                    dumbo_go = True
                    for i in neighbours(width, height, row, col):
                        grid[i[0]][i[1]] += 1
        if not dumbo_go:
            break
    # reset flashed dumbos
    for row, line in enumerate(grid):
        for col, dumbo in enumerate(line):
            if grid[row][col] > 9:
                grid[row][col] = 0
    # return grid after all possible flashes
    return grid


# PART 2
def part_two(file_name):
    grid = parse_data(file_name)
    dumbos = len(grid) * len(grid[0])
    step = 0
    while True:
        step += 1
        grid = flash(grid)
        if count_flashes(grid) == dumbos:
            break
    return step


def main(file_name):
    part_1 = part_one(file_name, 100)
    part_2 = part_two(file_name)
    return part_1, part_2


if __name__ == "__main__":
    part_1, part_2 = main("day_11_in.txt")
    print(f"Part one: {part_1}")
    print(f"Part two: {part_2}")
