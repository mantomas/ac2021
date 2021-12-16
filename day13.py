import re


def parse_data(file_name):
    with open(file_name, "r") as f:
        content = f.readlines()
        pairs = []
        steps = []
        for line in content:
            if re.match(r"\d+,\d+", line):
                pair = tuple(re.match(r"\d+,\d+", line.strip()).string.split(','))
                pairs.append(
                    (int(pair[0]), int(pair[1]))
                    )
            if '=' in line:
                fold = re.findall(r"(\w)=(\d+)", line)[0]
                steps.append((fold[0], int(fold[1])))
    return pairs, steps


# PART 1
def part_one(file_name):
    coords, foldings = parse_data(file_name)
    # foldig just once
    new_coords = []
    fold = foldings[0][1]
    if foldings[0][0] == "x":
        for i in coords:
            if i[0] > fold:
                new_coords.append(
                    (fold - (i[0] - fold), i[1])
                )
            else:
                new_coords.append(i)
    else:
        for i in coords:
            if i[1] > fold:
                new_coords.append(
                    (i[0], fold - (i[1] - fold))
                )
            else:
                new_coords.append(i)
    return len(set(new_coords))

# PART 2
def part_two(file_name):
    coords, foldings = parse_data(file_name)
    # foldig
    for fold in foldings:
        new_coords = []
        where = fold[1]
        if fold[0] == "x":
            for i in coords:
                if i[0] > where:
                    new_coords.append(
                        (where - (i[0] - where), i[1])
                    )
                else:
                    new_coords.append(i)
        else:
            for i in coords:
                if i[1] > where:
                    new_coords.append(
                        (i[0], where - (i[1] - where))
                    )
                else:
                    new_coords.append(i)
        coords = new_coords
    # size of output
    x_size = 0
    y_size = 0
    for i in coords:
        if i[0] > x_size:
            x_size = i[0]
        if i[1] > y_size:
            y_size = i[1]
    # print output
    for i in range(y_size + 1):
        for j in range(x_size + 1):
            if (j, i) in coords:
                print('#', end='')
            else:
                print(' ', end='')
        print()



def main(file_name):
    part_1 = part_one(file_name)
    return part_1


if __name__ == '__main__':
    part_1 = main("day_13_in.txt")
    print(f"Part one: {part_1}")
    part_two("day_13_in.txt")
