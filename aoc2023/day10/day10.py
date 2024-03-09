import os


def part_one(file):
    maze = []
    with open(os.path.join(os.path.dirname(__file__), file), "r", encoding="utf-8") as a_file:
        for a_line in a_file:
            a_line = a_line.strip()
            maze.append(a_line)
            if (s := a_line.find('S')) > -1:
                startx = s
                starty = len(maze) - 1

    nextx = startx
    nexty = starty
    heading = ''
    cell = ''
    steps = 0
    directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}

    # Determine start heading by looking around startpos for a valid direction to take
    for heading, (dx, dy) in directions.items():
        print(heading, dx, dy)
        if startx + dx >= 0:
            nextx += dx
        if starty + dy >= 0:
            nexty += dy
        cell = maze[nexty][nextx]
        if follow(heading, cell):
            break

    while True:
        steps += 1
        if nextx + dx >= 0:
            nextx += dx
        if nexty + dy >= 0:
            nexty += dy
        print('Going', heading, 'to', cell, 'at', nextx, nexty)
        if nextx == startx and nexty == starty:
            break
        cell = maze[nexty][nextx]
    # Should be back at 'S'
    print(steps)
    pass


def follow(heading, cell):
    # Enter 'cell' in direction 'heading'. Return a valid exit or false
    new_heading = False
    match (heading, cell):
        case ('N', '|') | ('E', 'J') | ('W', 'L'):
            new_heading = 'N'
        case ('N', 'F') | ('E', '-') | ('S', 'L'):
            new_heading = 'E'
        case ('E', '7') | ('S', '|') | ('W', 'F'):
            new_heading = 'S'
        case ('N', '7') | ('S', 'J') | ('W', '-'):
            new_heading = 'W'
    return new_heading


def test_follow():
    assert follow('N', '|') == 'N'
    assert follow('E', '|') is False


def test_part_one():
    part_one('day10_test.txt')
