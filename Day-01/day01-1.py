def main(puzzle_input):

    puzzle_input = puzzle_input.splitlines()
    solution = 0
    for val in puzzle_input:
        solution += ((int(val) / 3) - 2)

    return str(solution)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))