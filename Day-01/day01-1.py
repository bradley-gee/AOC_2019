def main(puzzle_input):

    puzzle_input = puzzle_input.splitlines()
    solution = 0
    for val in puzzle_input:
        solution += ((int(val) / 3) - 2)

    return str(solution)


with open("input.txt","r") as input_file:
    puzzle_input = input_file.read()
    print (main(puzzle_input))