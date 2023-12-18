# day05.py
import os
import re
import itertools


def part_one_two():
    seeds = []
    current_map = ''
    maps = {}
    valid_maps = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:',
                  'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:',
                  'humidity-to-location map:']

    # Parse input into a list of seeds and a collection of seed 'maps'
    with (open(os.path.join(os.path.dirname(__file__), 'day05_data.txt'), 'r', encoding='utf-8') as a_file):
        for a_line in a_file:
            a_line = a_line.strip()
            # Find seeds separately all on one line
            if (seed_line := a_line.split(':'))[0] == 'seeds':
                seeds = [int(x) for x in re.findall(r'\d+', seed_line[1])]
                continue
            # Note that the map has changed, values follow...
            if a_line in valid_maps:
                current_map = a_line
                continue
            # Add each of the map values to a dict of list of tuples
            if len(a_map := tuple([int(x) for x in re.findall(r'\d+', a_line)])):
                m = maps.get(current_map, [])
                m.append(a_map)
                maps[current_map] = m

    # Part One. Pass each seed through all the maps until a location is found. Find min location.
    def seed_to_location(seed):
        next_stage = seed
        for current_map in valid_maps:
            for dst, src, rgl in maps[current_map]:
                if src <= next_stage <= src + rgl:
                    next_stage = dst + next_stage - src
                    break
        return next_stage

    part_1_min_location = float('inf')
    for seed in seeds:
        part_1_min_location = min(part_1_min_location, seed_to_location(seed))

    print(part_1_min_location)

    # Part Two. Starting at location = 0 work back thru the map to find a seed, then check
    # if that's in the seed ranges. Stop if found. Still has the potential to get very big though.
    def location_to_seed(location):
        next_stage = location
        for current_map in reversed(valid_maps):
            for dst, src, rgl in maps[current_map]:
                if dst <= next_stage <= dst + rgl:
                    next_stage = src + next_stage - dst
                    break
        return next_stage

    part_2_min_location = 0
    found = False
    while not found:
        seed = location_to_seed(part_2_min_location)
        for batch in itertools.batched(seeds, 2):
            if batch[0] <= seed <= batch[0] + batch[1]:
                found = True
                break
        else:
            if part_2_min_location % 1000000 == 0:
                print(part_2_min_location)
            part_2_min_location += 1

    print(part_2_min_location)

    return part_1_min_location, part_2_min_location
