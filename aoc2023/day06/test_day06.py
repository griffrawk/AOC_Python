def test_part_one():
    race_length = 7
    race_record = 9

    speed_increment = 1

    for duration in range(0, race_length + 1):
        distance = duration * speed_increment * (race_length - duration)
        print('duration', duration, 'travels distance', distance)
