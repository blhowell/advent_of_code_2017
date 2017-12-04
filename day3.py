
"""
Advent of Code 2017
Python

Thanks to Tyler Tesch for helping make my code more effiecient/effective

# https://stackoverflow.com/questions/23706690/how-do-i-make-make-spiral-in-python
# http://adventofcode.com/2017/day/3
# use cycle to repeat move pattern indefinitely.
# use move pattern to generate pattern with differing movement from co-ords
# get:
# (1, (0, 0)) then R
# (2, (1, 0)) then U
# (3, (1, 1)) then L
# (4, (0, 1)) then L
# (5, (-1, 1)) then D
# (6, (-1, 0)) then D
# (7, (-1, -1)) then R
# (8, (0, -1)) then R
# (9, (1, -1)) then R
# (10, (2, -1)) then U
# etc...
# on an R apply multiplier! (number of rights to be done = number of times right has been done in mvement pattern += 1)
"""

from itertools import cycle


def part1(number):
    # movement_pattern = ("move_right", "move_up", "move_left", "move_down") make actual function calls....
    layer = 1           # spiral expansion
    coords = (0, 0)     # coords of number
    x = 1               # number that will be at coords position.

    def move_right(coords):
        return (coords[0] + 1, coords[1])

    def move_up(coords):
        return (coords[0], coords[1] + 1)

    def move_left(coords):
        return (coords[0] - 1, coords[1])

    def move_down(coords):
        return (coords[0], coords[1] - 1)

    movement_pattern = (move_right, move_up, move_left, move_down)

    for direction in cycle(movement_pattern):
        # handles expansion of spiral
        if direction == move_left:
            layer += 1
        if direction == move_right and x > 5:
            layer += 1

        for _ in range(layer):
            # call specific direction move's method the required number of times.
            # print("({}, {})".format(x, coords)) 
            coords = direction(coords)
            x += 1

            if x >= number:
                # print("({}, {})".format(x, coords)) 
                return abs(coords[0]) + abs(coords[1])


def part2(number):
    """Read data from first one and work from there?"""
    pass

# part1(325489)
print("Part One...", part1(325489))
print("Part Two...", part2(325489))
