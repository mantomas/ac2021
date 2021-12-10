def parse_data(file_name):
    with open(file_name, "r") as f:
        content = f.readlines()
        return [line.strip() for line in content]


# PART 1
def corrupted_points(line):
    opening = "([{<"
    closing = ")]}>"
    points = [3, 57, 1197, 25137]
    control = []
    for i in line:
        if i in opening:
            control.append(i)
        else:
            try:
                if closing.index(i) == opening.index(control[-1]):
                    control.pop()
                else:
                    return points[closing.index(i)]
            except Exception:
                return points[closing.index(i)]
    return 0


def part_one(file_name):
    data = parse_data(file_name)
    points = 0
    for line in data:
        points += corrupted_points(line)
    return points


# PART 2
def score(remaining):
    opening = "([{<"
    value = [1, 2, 3, 4]
    points = 0
    for i in remaining[::-1]:
        points *= 5
        points += value[opening.index(i)]
    return points


def points(line):
    opening = "([{<"
    control = []
    for i in line:
        if i in opening:
            control.append(i)
        else:
            control.pop()
    return score(control)            


def part_two(file_name):
    data = parse_data(file_name)
    scores = []
    for line in data:
        if corrupted_points(line) == 0:
            scores.append(points(line))
    winner_index = int((len(scores) - 1) / 2)
    return sorted(scores)[winner_index]


def main(file_name):
    part_1 = part_one(file_name)
    part_2 = part_two(file_name)
    return part_1, part_2


if __name__ == "__main__":
    part_1, part_2 = main("day_10_in.txt")
    print(f"Part one: {part_1}")
    print(f"Part two: {part_2}")
