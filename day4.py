def parse_data(file_name):
    with open(file_name, "r") as f:
        content = [line.strip() for line in f.readlines()]
    drawn_numbers = [int(number) for number in content[0].split(",")]
    boards = []
    board_helper = []
    for group in content[2:]:
        if len(group) > 0:
            board_helper.append([int(number) for number in group.split()])
            if len(board_helper) == 5:
                boards.append(board_helper)
                board_helper = []
    return drawn_numbers, boards


# PART 1


def winner_check(current_numbers, boards):
    for board in boards:
        for line in board:
            if all(number in current_numbers for number in line):
                return board
        for i in range(len(board[0])):
            if all(number in current_numbers for number in [line[i] for line in board]):
                return board
    return False


def calculate_score(winner, numbers_played):
    all_numbers = []
    for line in winner:
        all_numbers += line
    for number in numbers_played:
        try:
            all_numbers.remove(number)
        except ValueError:
            pass
    return sum(all_numbers) * numbers_played[-1]


def play(drawn_numbers, boards):
    # no need to check first four numbers
    numbers_played = drawn_numbers[:4]
    for number in drawn_numbers[4:]:
        numbers_played.append(number)
        possible_winner = winner_check(numbers_played, boards)
        if possible_winner:
            return calculate_score(possible_winner, numbers_played)
        else:
            continue


# PART 2


def board_check(board, current_numbers):
    for line in board:
        if all(number in current_numbers for number in line):
            return True
    for i in range(len(board[0])):
        if all(number in current_numbers for number in [line[i] for line in board]):
            return True
    return False


def win_last(drawn_numbers, boards):
    remaining_boards = boards
    # no need to check first four numbers
    numbers_played = drawn_numbers[:4]
    for number in drawn_numbers[4:]:
        new_remaining_boards = []
        numbers_played.append(number)
        for board in remaining_boards:
            if not board_check(board, numbers_played):
                new_remaining_boards.append(board)
        if len(new_remaining_boards) > 0:
            remaining_boards = new_remaining_boards
        else:
            return calculate_score(remaining_boards[0], numbers_played)


def main(input_filename):
    drawn_numbers, boards = parse_data(input_filename)
    print(f"First part answer: {play(drawn_numbers, boards)}")
    print(f"Seccond part answer: {win_last(drawn_numbers, boards)}")


if __name__ == '__main__':
    main("day_4_in.txt")
