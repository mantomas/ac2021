import re
import timeit
from collections import defaultdict


def parse_data(file_name):
    with open(file_name, "r") as f:
        content = [line.strip() for line in f.readlines()]
        list_of_tuples = [tuple(re.findall(r"\d+", line)) for line in content]
        return list_of_tuples


# map for PART 1
def make_map_hv(input_list):
    blank_map = [
        [0 for i in range(1000)] for j in range(1000)
    ]
    for line in input_list:
        # columns
        if line[0] == line[2]:
            line_points_y = [int(line[1]), int(line[3])]
            possition = int(line[0])
            for i in range(min(line_points_y), max(line_points_y) + 1):
                blank_map[i][possition] += 1
        # rows
        elif line[1] == line[3]:
            line_points_x = [int(line[0]), int(line[2])]
            line_number = int(line[1])
            for j in range(min(line_points_x), max(line_points_x) + 1):
                blank_map[line_number][j] += 1
    return blank_map


# PART 2 (version A)
def part_2_with_map(file_name):
    input_list = parse_data(file_name)
    blank_map = [
        [0 for i in range(1000)] for j in range(1000)
    ]
    for line in input_list:
        # columns
        if line[0] == line[2]:
            line_points_y = [int(line[1]), int(line[3])]
            possition = int(line[0])
            for i in range(min(line_points_y), max(line_points_y) + 1):
                blank_map[i][possition] += 1
        # rows
        elif line[1] == line[3]:
            line_points_x = [int(line[0]), int(line[2])]
            line_number = int(line[1])
            for j in range(min(line_points_x), max(line_points_x) + 1):
                blank_map[line_number][j] += 1
        # diagonals
        else:
            # X part
            line_points_x = (int(line[0]), int(line[2]))
            x_points = []
            for i in range(min(line_points_x), max(line_points_x) + 1):
                x_points.append(i)
            if int(line[0]) > int(line[2]):
                x_points.reverse()
            # Y part
            line_points_y = (int(line[1]), int(line[3]))
            y_points = []
            for i in range(min(line_points_y), max(line_points_y) + 1):
                y_points.append(i)
            if int(line[1]) > int(line[3]):
                y_points.reverse()
            # add points
            for row, column in zip(y_points, x_points):
                blank_map[row][column] += 1
    return count_over_two(blank_map)


def count_over_two(map_of_vents):
    more_than_one = 0
    for i in map_of_vents:
        for j in range(len(map_of_vents[0])):
            if i[j] > 1:
                more_than_one += 1
    return more_than_one


# PART 2 (version B) - less work (no blank map)
def part_2_defaultdict(file_name):
    input_list = parse_data(file_name)
    vents = defaultdict(int)
    for line in input_list:
        # columns
        if line[0] == line[2]:
            line_points_y = [int(line[1]), int(line[3])]
            possition = int(line[0])
            for i in range(min(line_points_y), max(line_points_y) + 1):
                vents[(i, possition)] += 1
        # rows
        elif line[1] == line[3]:
            line_points_x = [int(line[0]), int(line[2])]
            line_number = int(line[1])
            for j in range(min(line_points_x), max(line_points_x) + 1):
                vents[(line_number, j)] += 1
        # diagonals
        else:
            # X part
            line_points_x = (int(line[0]), int(line[2]))
            x_points = []
            for i in range(min(line_points_x), max(line_points_x) + 1):
                x_points.append(i)
            if int(line[0]) > int(line[2]):
                x_points.reverse()
            # Y part
            line_points_y = (int(line[1]), int(line[3]))
            y_points = []
            for i in range(min(line_points_y), max(line_points_y) + 1):
                y_points.append(i)
            if int(line[1]) > int(line[3]):
                y_points.reverse()
            # add points
            for row, column in zip(y_points, x_points):
                vents[(row, column)] += 1
    return len([value for value in vents.values() if value > 1])


def main(file_name):
    input_list = parse_data(file_name)
    map_of_vents = make_map_hv(input_list)
    part_1 = count_over_two(map_of_vents)
    part_2 = part_2_with_map(file_name)
    return part_1, part_2


if __name__ == '__main__':
    part1, part2 = main('day_5_in.txt')
    print(f"Part one: {part1}")
    print(f"Part two: {part2}")
    print("Speed comparison")
    print("Part two_A:", timeit.timeit(
        "part_2_with_map('day_5_in.txt')",
        setup="from __main__ import part_2_with_map",
        number=1)
        )
    print("Part two_B:", timeit.timeit(
        "part_2_defaultdict('day_5_in.txt')",
        setup="from __main__ import part_2_defaultdict",
        number=1)
        )
