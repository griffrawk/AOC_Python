# day06.py

def test_part_one():
    # races = [(7, 9), (15, 40), (30, 200)]
    # races = [(47, 400), (98, 1213), (66, 1011), (98, 1540)]
    races = [(47986698, 400121310111540)]
    speed_increment = 1
    margin = 1

    for race_length, race_record in races:
        ways_to_win = 0
        for duration in range(0, race_length + 1):
            distance = duration * speed_increment * (race_length - duration)
            if distance >= race_record:
                ways_to_win += 1
            # Stop looping if distance has peaked and dropped below record
            if distance < race_record and ways_to_win > 1:
                break
        margin = margin * ways_to_win
        print('ways', ways_to_win)
    
    print('margin', margin)
    # assert margin == 288
    # assert margin == 1660968
    assert margin == 26499773