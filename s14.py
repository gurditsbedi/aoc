
from collections import namedtuple

Point = namedtuple('Point', 'x y')


class Point(Point):
    def __repr__(self):
        return f'({self.x}, {self.y})'


def path_as_set(path):
    ps = set()
    for i in range(len(path)-1):
        p1, p2 = path[i], path[i+1]
        if p1.x == p2.x:
            ymin, ymax = sorted([p1.y, p2.y])
            linepath = set(Point(p1.x, y) for y in range(ymin, ymax+1))
        elif p1.y == p2.y:
            xmin, xmax = sorted([p1.x, p2.x])
            linepath = set(Point(x, p1.y) for x in range(xmin, xmax+1))
        ps = ps | linepath
    return ps


f = open("in14.txt")
path = set()
for line in f:
    points = [Point(*map(int, (ord for ord in p.split(','))))
              for p in line.strip().split(' ') if p != "->"]
    ps = path_as_set(points)
    path = path | ps

ymax = max(p.y for p in path)

# part 1
sands = set()
sand = Point(500, 0)
while sand.y < ymax:
    moved = False
    next_possible_sand = [
        Point(sand.x, sand.y + 1),
        Point(sand.x - 1, sand.y + 1),
        Point(sand.x + 1, sand.y + 1),
    ]
    for nps in next_possible_sand:
        if nps not in (path | sands):
            sand = nps
            moved = True
            break

    if not moved:
        sands.add(sand)
        sand = Point(500, 0)

print(len(sands))

# part 2
new_ymax = ymax + 2
sand_row = set()
next_sand_row = set([Point(500, 0)])

count = 1
for y in range(new_ymax-1):
    sand_row = next_sand_row
    next_sand_row = set()

    for sand in sand_row:
        next_possible_sands = [
            Point(sand.x - 1, sand.y + 1),
            Point(sand.x, sand.y + 1),
            Point(sand.x + 1, sand.y + 1),
        ]

        for nps in next_possible_sands:
            if nps not in path:
                next_sand_row.add(nps)
    count += len(next_sand_row)

print(count)
