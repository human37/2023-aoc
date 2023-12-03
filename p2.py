MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def valid(draw):
    for cube in draw:
        num, color = cube.split()
        if color == "red" and int(num) > MAX_RED:
            return False
        if color == "green" and int(num) > MAX_GREEN:
            return False
        if color == "blue" and int(num) > MAX_BLUE:
            return False
    return True


def find_num(draw):
    red = 0
    green = 0
    blue = 0
    for cube in draw:
        num, color = cube.split()
        if color == "red" and int(num) > red:
            red = int(num)
        if color == "green" and int(num) > green:
            green = int(num)
        if color == "blue" and int(num) > blue:
            blue = int(num)
    return red, green, blue


def calc_power(min_red, min_green, min_blue):
    return min_red * min_green * min_blue


def p1():
    possible_games_sum = 0
    with open("p2-input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            game_id = int(line.split(" ")[1][:-1])
            games = line.split(": ")[1].split(";")
            for game in games:
                draw = game.split(",")
                if not valid(draw):
                    break
            else:
                possible_games_sum += game_id
    return possible_games_sum


def p2():
    min_sets_power_sum = 0
    with open("p2-input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            game = line.split(": ")[1].split(";")
            reds, greens, blues = [], [], []
            for draw in game:
                draw = draw.split(",")
                red, green, blue = find_num(draw)
                reds.append(red)
                greens.append(green)
                blues.append(blue)
            min_sets_power_sum += calc_power(max(reds), max(greens), max(blues))
    return min_sets_power_sum


def main():
    print("possible games ID sum: ", p1())
    print("min sets power sum: ", p2())


if __name__ == "__main__":
    main()
