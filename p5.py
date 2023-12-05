def read_input():
    seeds_list = []
    seed_mappings = {}
    with open("p5-input.txt") as f:
        line = f.readline()
        line = line.strip().split()
        seeds_list = [int(x) for x in line[1:]]
        f.readline()
        f.readline()
        seeds_to_soil = create_map(f)
        seed_mappings["seeds_to_soil"] = seeds_to_soil
        soil_to_fertilizer = create_map(f)
        seed_mappings["soil_to_fertilizer"] = soil_to_fertilizer
        fertilizer_to_water = create_map(f)
        seed_mappings["fertilizer_to_water"] = fertilizer_to_water
        water_to_light = create_map(f)
        seed_mappings["water_to_light"] = water_to_light
        light_to_temperature = create_map(f)
        seed_mappings["light_to_temperature"] = light_to_temperature
        temperature_to_humidity = create_map(f)
        seed_mappings["temperature_to_humidity"] = temperature_to_humidity
        humidity_to_location = create_map(f)
        seed_mappings["humidity_to_location"] = humidity_to_location
    return seeds_list, seed_mappings


def entry(rs, rl):
    return (int(rs), int(rs) + int(rl) - 1)


def create_map(f):
    map = {}
    line = f.readline().strip()
    while line != "":
        destination_rs, source_rs, rl = line.strip().split()
        map[entry(source_rs, rl)] = entry(destination_rs, rl)
        line = f.readline().strip()
    f.readline()
    return map


def in_range(num, range):
    return num >= range[0] and num <= range[1]


def find_destination(seed, mappings, current):
    dest = 0
    for key in mappings[current]:
        if in_range(seed, key):
            dest = seed - key[0] + mappings[current][key][0]
            break
    else:
        dest = seed
    return dest


def find_location(seed, mappings):
    soil_num = find_destination(seed, mappings, "seeds_to_soil")
    fertilizer_num = find_destination(soil_num, mappings, "soil_to_fertilizer")
    water_num = find_destination(fertilizer_num, mappings, "fertilizer_to_water")
    light_num = find_destination(water_num, mappings, "water_to_light")
    temp_num = find_destination(light_num, mappings, "light_to_temperature")
    humidity_num = find_destination(temp_num, mappings, "temperature_to_humidity")
    location_num = find_destination(humidity_num, mappings, "humidity_to_location")
    return location_num


def p1():
    seeds_list, seed_mappings = read_input()
    locations = []
    for seed in seeds_list:
        location = find_location(seed, seed_mappings)
        locations.append(location)
    return min(locations)


def main():
    print("lowest location number: ", p1())


if __name__ == "__main__":
    main()
