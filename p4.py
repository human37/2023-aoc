SCRATCHCARDS = {}


def read_input():
    with open("p4-input.txt") as f:
        return f.readlines()


def calc_power(num):
    s = 1
    if num == 0:
        return 0
    for _ in range(1, num):
        s *= 2
    return s


def make_key(card_number):
    return f"CARD-{card_number}"


def add_scratchcard(card_number):
    global SCRATCHCARDS
    key = make_key(card_number)
    if key in SCRATCHCARDS:
        current_num = SCRATCHCARDS.get(key)
        SCRATCHCARDS[key] = current_num + 1
    else:
        SCRATCHCARDS[key] = 1


def add_scratchcards(starting_number, num_winning_scratchcards):
    global SCRATCHCARDS
    for num in range(1, num_winning_scratchcards + 1):
        add_scratchcard(starting_number + num)


def sum_scratchcards():
    global SCRATCHCARDS
    s = 0
    for key in SCRATCHCARDS:
        s += SCRATCHCARDS[key]
    return s


def p1():
    scratchcards_points_sum = 0
    lines = read_input()
    for line in lines:
        winning_numbers, your_numbers = line.split("|")
        winning_numbers = winning_numbers.split(":")[1].strip().split()
        your_numbers = your_numbers.strip().split()
        num_winning_numbers = 0
        for num in your_numbers:
            if num in winning_numbers:
                num_winning_numbers += 1
        scratchcards_points_sum += calc_power(num_winning_numbers)
    return scratchcards_points_sum


def p2():
    lines = read_input()
    for line in lines:
        winning_numbers, your_numbers = line.split("|")
        winning_numbers = winning_numbers.split(":")[1].strip().split()
        card_number = int(line.split()[1][:-1])
        your_numbers = your_numbers.strip().split()
        num_winning_numbers = 0
        for num in your_numbers:
            if num in winning_numbers:
                num_winning_numbers += 1
        add_scratchcard(card_number)  # add initial scratchcard
        if (
            SCRATCHCARDS.get(make_key(card_number))
            and SCRATCHCARDS[make_key(card_number)] > 0
        ):
            # we have multiple instances of the same card
            for _ in range(SCRATCHCARDS[make_key(card_number)]):
                add_scratchcards(card_number, num_winning_numbers)
        else:
            add_scratchcards(card_number, num_winning_numbers)
    return sum_scratchcards()


def main():
    print("scratchcards points sum: ", p1())
    print("number of scratchcards with the new rules: ", p2())


if __name__ == "__main__":
    main()
