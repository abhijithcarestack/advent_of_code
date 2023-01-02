from ast import literal_eval

SOURCE_LOCATION = (500, 0)
AIR = "."
ROCK = "#"
SAND = "o"
SOURCE = "+"


def neighbours(x, y):
    for dx in [0, -1, 1]:
        yield x + dx, y + 1


def release_sand(cave, sand, condition, space_is_open):
    while condition():
        if open_neighbours := [n for n in neighbours(*sand[-1]) if space_is_open(n)]:
            sand.append(open_neighbours[0])
        else:
            cave[sand.pop()] = SAND


def is_inside(x, y):
    return x_min <= x <= x_max and y_min <= y <= y_max


cave = open("inputs.txt", "r").read().split('\n')
cave = [[literal_eval(coord) for coord in line.split(" -> ")] for line in cave]
cave = {
    (x, y): ROCK
    for path in cave
    for (x1, y1), (x2, y2) in zip(path, path[1:])
    for x in range(min(x1, x2), max(x1, x2) + 1)
    for y in range(min(y1, y2), max(y1, y2) + 1)
}
cave[SOURCE_LOCATION] = SOURCE

x_min, x_max = sorted(key[0] for key in cave)[::len(cave) - 1]
y_min, y_max = sorted(key[1] for key in cave)[::len(cave) - 1]

sand_path = [SOURCE_LOCATION]
release_sand(cave, sand_path, lambda: is_inside(
    *sand_path[-1]), lambda r: r not in cave)
print(sum(1 for val in cave.values() if val == SAND))

floor = y_max + 2
release_sand(cave, sand_path, lambda: sand_path,
             lambda r: r[1] < floor and r not in cave)
print(sum(1 for val in cave.values() if val == SAND))
