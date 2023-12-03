def read_input():
    lines = []
    with open("p3-input.txt") as f:
        for line in f.readlines():
            l = []
            l.extend(line.strip())
            lines.append(l)
    return lines


def read_number(engine, x, y):
    num = ""
    while x < len(engine[y]) and engine[y][x].isdigit():
        num += engine[y][x]
        x += 1
    return num


def is_symbol(char):
    return not char.isdigit() and char != "."


def is_gear(char):
    return char == "*"


def find_full_number(engine, x, y):
    while x >= 0 and engine[y][x].isdigit():
        x -= 1
    a, b = read_number(engine, x + 1, y), (x + 1, y)
    return a, b


def is_part_number(engine, x, y, num_length):
    for _ in range(num_length):
        # check up
        if y - 1 >= 0 and is_symbol(engine[y - 1][x]):
            return True
        # check down
        if y + 1 < len(engine) and is_symbol(engine[y + 1][x]):
            return True
        # check left
        if x - 1 >= 0 and is_symbol(engine[y][x - 1]):
            return True
        # check right
        if x + 1 < len(engine[y]) and is_symbol(engine[y][x + 1]):
            return True
        # check up left diagonal
        if y - 1 >= 0 and x - 1 >= 0 and is_symbol(engine[y - 1][x - 1]):
            return True
        # check up right diagonal
        if y - 1 >= 0 and x + 1 < len(engine[y]) and is_symbol(engine[y - 1][x + 1]):
            return True
        # check down left diagonal
        if y + 1 < len(engine) and x - 1 >= 0 and is_symbol(engine[y + 1][x - 1]):
            return True
        # check down right diagonal
        if (
            y + 1 < len(engine)
            and x + 1 < len(engine[y])
            and is_symbol(engine[y + 1][x + 1])
        ):
            return True
        x += 1
    return False


def num_is_gear(engine, x, y, num_length):
    for _ in range(num_length):
        # check up
        if y - 1 >= 0 and is_gear(engine[y - 1][x]):
            return True, (x, y - 1)
        # check down
        if y + 1 < len(engine) and is_gear(engine[y + 1][x]):
            return True, (x, y + 1)
        # check left
        if x - 1 >= 0 and is_gear(engine[y][x - 1]):
            return True, (x - 1, y)
        # check right
        if x + 1 < len(engine[y]) and is_gear(engine[y][x + 1]):
            return True, (x + 1, y)
        # check up left diagonal
        if y - 1 >= 0 and x - 1 >= 0 and is_gear(engine[y - 1][x - 1]):
            return True, (x - 1, y - 1)
        # check up right diagonal
        if y - 1 >= 0 and x + 1 < len(engine[y]) and is_gear(engine[y - 1][x + 1]):
            return True, (x + 1, y - 1)
        # check down left diagonal
        if y + 1 < len(engine) and x - 1 >= 0 and is_gear(engine[y + 1][x - 1]):
            return True, (x - 1, y + 1)
        # check down right diagonal
        if (
            y + 1 < len(engine)
            and x + 1 < len(engine[y])
            and is_gear(engine[y + 1][x + 1])
        ):
            return True, (x + 1, y + 1)
        x += 1
    return False, None


def find_gear_pair(engine, first_pair_coords, gear_coords):
    x, y = gear_coords
    # check up
    if y - 1 >= 0 and engine[y - 1][x].isdigit():
        num, coords = find_full_number(engine, x, y - 1)
        if coords != first_pair_coords:
            return num, coords
    # check down
    if y + 1 < len(engine) and engine[y + 1][x].isdigit():
        num, coords = find_full_number(engine, x, y + 1)
        if coords != first_pair_coords:
            return num, coords
    # check left
    if x - 1 >= 0 and engine[y][x - 1].isdigit():
        num, coords = find_full_number(engine, x - 1, y)
        if coords != first_pair_coords:
            return num, coords
    # check right
    if x + 1 < len(engine[y]) and engine[y][x + 1].isdigit():
        num, coords = find_full_number(engine, x + 1, y)
        if coords != first_pair_coords:
            return num, coords
    # check up left diagonal
    if y - 1 >= 0 and x - 1 >= 0 and engine[y - 1][x - 1].isdigit():
        num, coords = find_full_number(engine, x - 1, y - 1)
        if coords != first_pair_coords:
            return num, coords
    # check up right diagonal
    if y - 1 >= 0 and x + 1 < len(engine[y]) and engine[y - 1][x + 1].isdigit():
        num, coords = find_full_number(engine, x + 1, y - 1)
        if coords != first_pair_coords:
            return num, coords
    # check down left diagonal
    if y + 1 < len(engine) and x - 1 >= 0 and engine[y + 1][x - 1].isdigit():
        num, coords = find_full_number(engine, x - 1, y + 1)
        if coords != first_pair_coords:
            return num, coords
    # check down right diagonal
    if (
        y + 1 < len(engine)
        and x + 1 < len(engine[y])
        and engine[y + 1][x + 1].isdigit()
    ):
        num, coords = find_full_number(engine, x + 1, y + 1)
        if coords != first_pair_coords:
            return num, coords
    return None, None


def p1():
    part_numbers_sum = 0
    engine = read_input()
    for y in range(len(engine)):
        for x in range(len(engine[y]) - 1):
            char = engine[y][x]
            if (
                x == 0
                and char.isdigit()
                or not engine[y][x - 1].isdigit()
                and char.isdigit()
            ):
                # we are at the beginning of a number
                num = read_number(engine, x, y)
                if is_part_number(engine, x, y, len(num)):
                    part_numbers_sum += int(num)
    return part_numbers_sum


def p2():
    gear_ratios_sum = 0
    added_gears = []
    engine = read_input()
    for y in range(len(engine)):
        for x in range(len(engine[y]) - 1):
            char = engine[y][x]
            if (
                x == 0
                and char.isdigit()
                or not engine[y][x - 1].isdigit()
                and char.isdigit()
            ):
                # we are at the beginning of a number
                num1 = read_number(engine, x, y)
                num1_coords = (x, y)
                is_gear, gear_coords = num_is_gear(engine, x, y, len(num1))
                if is_gear:
                    if num1_coords in added_gears:
                        continue
                    added_gears.append(num1_coords)
                    num2, coords = find_gear_pair(engine, num1_coords, gear_coords)
                    if coords != None and coords not in added_gears:
                        added_gears.append(coords)
                        gear_ratios_sum += int(num1) * int(num2)
    return gear_ratios_sum


def main():
    print("part numbers sum: ", p1())
    print("gear ratios sum: ", p2())


if __name__ == "__main__":
    main()
