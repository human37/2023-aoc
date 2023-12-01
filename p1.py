import operator


def read_input():
    with open("p1-input.txt") as f:
        return f.readlines()


def p1():
    lines = read_input()
    calibration_sum = 0
    for line in lines:
        current_line_nums = []
        for char in line:
            if char.isnumeric():
                current_line_nums.append(char)
        calibration = str(current_line_nums[0]) + str(current_line_nums[-1])
        calibration_sum += int(calibration)
    return calibration_sum


def p2():
    lines = read_input()
    calibration_sum = 0
    str_num_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for line in lines:
        current_line_nums = []
        index = 0
        for num in str_num_map:
            left_found_index = str.find(line, num)
            if left_found_index != -1:
                current_line_nums.append(
                    {"found_index": left_found_index, "value": str_num_map[num]}
                )
            right_found_index = str.rfind(line, num)
            if right_found_index != -1:
                current_line_nums.append(
                    {"found_index": right_found_index, "value": str_num_map[num]}
                )
        for char in line:
            if char.isnumeric():
                current_line_nums.append({"found_index": index, "value": int(char)})
            index += 1
        current_line_nums = sorted(
            current_line_nums, key=operator.itemgetter("found_index")
        )
        calibration = str(current_line_nums[0]["value"]) + str(
            current_line_nums[-1]["value"]
        )
        calibration_sum += int(calibration)
    return calibration_sum


print(p2())
