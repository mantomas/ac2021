from ..day15 import create_graph, parse_data, part_one, part_two


def test_parse_data():
    maze = parse_data("tests/data_test_day_15.txt")
    assert isinstance(maze, list)
    assert len(maze) == 10
    assert maze[0][0] == 1
    assert maze[9][9] == 1
    assert maze[9][0] == 2


def test_create_graph():
    grid = parse_data("tests/data_test_day_15.txt")
    graph = create_graph(grid)
    assert graph[(0, 0)] == {(0, 1): 1, (1, 0): 1}
    assert graph[(9, 9)] == {(8, 9): 1, (9, 8): 8}


def test_part_one():
    grid = parse_data("tests/data_test_day_15.txt")
    assert part_one(grid, (9, 9)) == 40


def test_part_two():
    grid = parse_data("tests/data_test_day_15.txt")
    assert part_two(grid, (49, 49)) == 315
