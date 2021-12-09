import math


def parse_data_part_one(file_name):
    with open(file_name, "r") as f:
        lol = []
        for line in f.readlines():
            lol.append([int(num) for num in line.strip()])
        return lol


# PART 1
def part_one(file_name):
    low_point = 0
    data = parse_data_part_one(file_name)
    max_row = len(data) - 1
    max_column = len(data[0]) - 1
    for i, line in enumerate(data):
        for j, point in enumerate(line):
            # fields around
            group = []
            if i > 0:
                group.append(data[i - 1][j])
            if j > 0:
                group.append(data[i][j - 1])
            if j < max_column:
                group.append(data[i][j + 1])
            if i < max_row:
                group.append(data[i + 1][j])
            # final decision
            if point < min(group):
                low_point += point + 1
    return low_point


# PART 2
def get_coordinates(data):
    """Calculate all low locations"""
    coordinates = []
    max_row = len(data) - 1
    max_column = len(data[0]) - 1
    for i, line in enumerate(data):
        for j, point in enumerate(line):
            # fields around
            group = []
            if i > 0:
                group.append(data[i - 1][j])
            if j > 0:
                group.append(data[i][j - 1])
            if j < max_column:
                group.append(data[i][j + 1])
            if i < max_row:
                group.append(data[i + 1][j])
            # final decision
            if point < min(group):
                coordinates.append((i, j, point))
    return coordinates


def get_field(coordinate, data):
    """Create local basin map and blank map the same size"""
    row, column, base = coordinate
    max_row = len(data) - 1
    max_column = len(data[0]) - 1
    top = row - (8 - base) if row - (8 - base) > 0 else 0
    bottom = row + (8 - base) if row + (8 - base) < max_row else max_row
    left = column - (8 - base) if column - (8 - base) > 0 else 0
    right = column + (8 - base) if column + (8 - base) < max_column else max_column
    field_in = []
    for i in range(top, bottom + 1):
        line = []
        for j in range(left, right + 1):
            line.append(data[i][j])
        field_in.append(line)
    field_out = []
    for i in range(top, bottom + 1):
        field_out.append([9 for i in range(left, right + 1)])
    x = row - top
    y = column - left
    field_out[x][y] = base
    return field_in, field_out


def mark_neighbours(fin, fout):
    """Write basin to local map"""
    test = 9
    while test > 0:
        for row, line in enumerate(fin):
            for col, num in enumerate(line):
                if (
                    (row - 1 >= 0 and 9 > fin[row][col] > fout[row - 1][col])
                    or (col - 1 >= 0 and 9 > fin[row][col] > fout[row][col - 1] < 9)
                    or (col + 1 <= len(fin[0]) - 1 and 9 > fin[row][col] > fout[row][col + 1] < 9)
                    or (row + 1 <= len(fin) - 1 and 9 > fin[row][col] > fout[row + 1][col] < 9)
                ):
                    fout[row][col] = num
        test -= 1
    return fout


def calculate_size(coordinate, data):
    """Helper function to calculate basin size"""
    field_in, field_out = get_field(coordinate, data)
    field_out = mark_neighbours(field_in, field_out)
    # final count of single basin
    below_nine = 0
    for row in field_out:
        for column in row:
            if column < 9:
                below_nine += 1
    return below_nine


def part_two(file_name):
    """Put things together and return product of three bigest basins"""
    sizes = []
    data = parse_data_part_one(file_name)
    coordinates = get_coordinates(data)
    for coordinate in coordinates:
        sizes.append(calculate_size(coordinate, data))
    max_three = sorted(sizes)[-3:]
    return math.prod(max_three)


def main(file_name):
    part_1 = part_one(file_name)
    part_2 = part_two(file_name)
    return part_1, part_2


if __name__ == "__main__":
    part_1, part_2 = main("day_9_in.txt")
    print(f"Part one: {part_1}")
    print(f"Part two: {part_2}")
