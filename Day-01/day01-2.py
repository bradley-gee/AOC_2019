def main(puzzle_input):

    puzzle_input = puzzle_input.splitlines()
    solution = 0
    for val in puzzle_input:
        solution += get_fuel_for_mass(int(val))
    return str(solution)

def get_fuel_for_mass(added_mass):
    fuel_for_added_mass = (added_mass // 3) - 2
    if fuel_for_added_mass > 0:
        fuel_for_added_mass += get_fuel_for_mass(fuel_for_added_mass)
    else:
        return 0

    return fuel_for_added_mass


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))