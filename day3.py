from collections import defaultdict

with open("day_3_in.txt", "r") as f:
    content = [line.strip() for line in f.readlines()]

# PART ONE

# counting 1 on possition 1-12
numbers = defaultdict(int)
for line in content:
    for i, j in enumerate(line):
        numbers[i] += int(j)


# constructing gamma/epsilon numbers
gamma = []
epsilon = []
for number in numbers.values():
    if number > len(content) / 2:
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")

print(int("".join(gamma), 2) * int("".join(epsilon), 2))


# PART TWO


def filter_most_common(max_content=None):
    if max_content is None:
        max_content = content
    for possition in range(len(content[0])):
        ones = 0
        zeroes = 0
        for line in max_content:
            if line[possition] == "1":
                ones += 1
            else:
                zeroes += 1
        if ones < zeroes:
            maximal = "0"
        else:
            maximal = "1"
        max_content = [line for line in max_content if line[possition] == maximal]
        if len(max_content) == 1:
            return max_content[0]


def filter_least_common(min_content=None):
    if min_content is None:
        min_content = content
    for possition in range(len(content[0])):
        ones = 0
        zeroes = 0
        for line in min_content:
            if line[possition] == "1":
                ones += 1
            else:
                zeroes += 1
        if ones < zeroes:
            minimal = "1"
        else:
            minimal = "0"
        min_content = [line for line in min_content if line[possition] == minimal]
        if len(min_content) == 1:
            return min_content[0]


oxygen = filter_most_common()
co2 = filter_least_common()
print(int(oxygen, 2) * int(co2, 2))
