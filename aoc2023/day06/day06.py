# day06.py
import math


def part_one_two():
    # races = [(7, 9), (15, 40), (30, 200)]
    # races = [(47, 400), (98, 1213), (66, 1011), (98, 1540)]
    races = [(47986698, 400121310111540)]
    margin = 1

    for race_length, race_record in races:
        # ways_to_win = 0
        # for button_time in range(0, race_length + 1):
        #     distance = button_time * (race_length - button_time)
        #     if distance >= race_record:
        #         ways_to_win += 1
        #     # Stop looping if distance has peaked and dropped below record
        #     if distance < race_record and ways_to_win > 1:
        #         break

        # Quadratic equation:
        # The looped code increments ways_to_win when distance > race_record
        # where distance = button_time * ( race_length - button_time)
        #
        # This can be expressed as:
        # distance = -(button_time ** 2) + race_length * button_time
        #
        # Solving for values of button_time when distance = 0 gives you upper & lower
        # limits for ways_to_win = upper - lower - 1
        #
        # The last -1 is to account for the fact that you are supposed to exceed the
        # previous record, otherwise ways_to_win would include the previous record.

        x1 = math.sqrt(race_length * race_length - 4 * race_record)
        lower_button_time = math.floor((race_length - x1) / 2)
        upper_button_time = math.ceil((x1 + race_length) / 2)
        ways_to_win = upper_button_time - lower_button_time - 1
        margin = margin * ways_to_win
        print("ways", ways_to_win)

    return margin
