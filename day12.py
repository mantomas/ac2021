from collections import defaultdict


# graph of connections
def parse_data(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    graph = defaultdict(list)
    for line in content:
        ends = line.strip().split('-')
        graph[ends[0]].append(ends[1])
        graph[ends[1]].append(ends[0])
    return graph


# PART 1 - Depth First Search
def part_one(file_name):
    graph = parse_data(file_name)
    global paths
    paths = set()
    dfs(graph, 'start', 'end')
    return len(paths)


# DFS recursion
def dfs(graph, start, end, path=tuple()):
    path = path+(start, )
    if start == end:
        paths.add(path)
    else:
        for node in graph[start]:
            if node.isupper() or node not in path:
                dfs(graph, node, end, path)


# PART 2
def part_two(file_name):
    graph = parse_data(file_name)
    global paths
    paths = set()
    dfs_B(graph, 'start', 'end')
    return len(paths)


def dfs_B(graph, start, end, path=tuple()):
    path = path + (start, )
    if start == end:
        paths.add(path)
    else:
        for node in graph[start]:
            if node.isupper() or node not in path:
                dfs_B(graph, node, end, path)
            elif node not in ['start', 'end']:
                helper = 0
                for i in list(set(path)):
                    if i.islower() and path.count(i) > 1:
                        helper += 1
                if helper < 1:
                    dfs_B(graph, node, end, path)


if __name__ == '__main__':
    part_1 = part_one("day_12_in.txt")
    part_2 = part_two("day_12_in.txt")
    print(f"Part one: {part_1}")
    print(f"Part two: {part_2}")
