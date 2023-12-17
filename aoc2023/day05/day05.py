# day05.py
import os
import re


def part_one():
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
                seeds = re.findall(r'\d+', seed_line[1])
                continue
            # Note that the map has changed
            if a_line in valid_maps:
                current_map = a_line
                continue
            # Add each of the map lines to a dict of list of tuples
            if len(a_map := tuple([int(x) for x in re.findall(r'\d+',a_line)])):
                m = maps.get(current_map, [])
                m.append(a_map)
                maps[current_map] = m

    def seed_to_location():
        # Pass each seed through all the maps until a location is found. Find min location.
        min_location = float('inf')
        for seed in seeds:
            next_stage = int(seed)
            for current_map in valid_maps:
                for dst, src, rgl in maps[current_map]:
                    if src <= next_stage <= src + rgl:
                        # print('modified by', current_map)
                        next_stage = dst + next_stage - src
                        break
                # print('next stage', next_stage)
            # print('seed', seed, 'location', next_stage)
            min_location = min(min_location, next_stage)
        print(min_location)
        return min_location

    part1 = seed_to_location()

    # now mangle the seed list for part_two rules and rerun the map

    return part1
