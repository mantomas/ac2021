import re
from collections import defaultdict
from typing import DefaultDict, List, Tuple


def parse_data(file_name: str) -> List[int]:
    with open(file_name, "r") as f:
        numbers = [int(i) for i in re.findall(r"\d+", f.read())]
        return numbers


# PART 1 - slow version :D
def part_one(initial: List[int], repeat: int) -> int:
    fishes = initial
    for _ in range(repeat):
        new_lf_count: int = fishes.count(0)
        new_fishes: List[int] = []
        for lf in fishes:
            if lf > 0:
                new_fishes.append(lf - 1)
            else:
                new_fishes.append(6)
        for _baby in range(new_lf_count):
            new_fishes.append(8)
        fishes = new_fishes
    return len(fishes)


# PART 2 - mač betr
def part_two(initial: List[int], repeat: int) -> int:
    data: DefaultDict[int, int] = defaultdict(int)
    # initial dataset
    for i in initial:
        data[i] += 1
    # counting days
    for _ in range(repeat):
        new_fishes: int = data[0]
        for i in range(8):
            data[i] = data[i + 1]
        data[6] += new_fishes
        data[8] = new_fishes
    return sum(data.values())


def main(file_name: str) -> Tuple[int, int]:
    data = parse_data(file_name)
    l_fish = part_one(data, 80)
    l_fish_part_two = part_two(data, 256)
    return l_fish, l_fish_part_two


if __name__ == "__main__":
    part_1, part_2 = main("day_6_in.txt")
    print(f"Part one: {part_1}")
    print(f"Part two: {part_2}")
