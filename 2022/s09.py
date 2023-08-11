from collections import namedtuple

Point = namedtuple('Point', 'x y')


class Point(Point):
    def __repr__(self):
        return f'({self.x}, {self.y})'


def m(rope):
    x = [p.x for p in rope]
    y = [p.y for p in rope]
    min_x = min(x)
    min_y = min(y)
    max_x = max(x)
    max_y = max(y)
    C = max_x - min_x + 1
    R = max_y - min_y + 1
    ll = [['.' for y in range(C)] for x in range(R)]
    for i, p in enumerate(rope):
        xx = p.x - min_x
        yy = p.y - min_y
        if ll[R-yy-1][xx] == '.':
            ll[R - yy-1][xx] = str(i)

    return "\n".join(''.join(x) for x in ll)


movement = dict(U=Point(0, 1), D=Point(0, -1),
                L=Point(-1, 0), R=Point(1, 0))

f = open('in09.txt', 'r')

h = Point(0, 0)
t = Point(0, 0)
travel = set()
for line in f.readlines():
    dir, dis = line.strip().split()
    dis = int(dis)
    # move H
    for step in range(dis):
        h = Point(h.x + movement[dir].x, h.y + movement[dir].y)
        diff = Point(abs(h.x - t.x), abs(h.y - t.y))
        ht_dist = diff.x + diff.y
        if diff == Point(2, 0) or diff == Point(0, 2):  # straight movement
            t = Point(t.x + movement[dir].x, t.y + movement[dir].y)
        elif diff == Point(2, 1) or diff == Point(1, 2):  # diagonal movement
            if diff.x == 1:
                t = Point(h.x, t.y - (1 if t.y > h.y else -1))
            elif diff.y == 1:
                t = Point(t.x - (1 if t.x > h.x else -1), h.y)
        travel.add(t)

print(len(travel))

f.seek(0)
count = 10
rope = [Point(0, 0) for x in range(count)]

travel = set()
for line in f.readlines():
    dir, dis = line.strip().split()
    dis = int(dis)
    for step in range(dis):
        rope[0] = Point(rope[0].x + movement[dir].x,
                        rope[0].y + movement[dir].y)
        for i in range(count-1):
            h = rope[i]
            t = rope[i+1]

            diff = Point(abs(h.x - t.x), abs(h.y - t.y))
            if diff.x < 1 and diff.y < 1:
                continue
            elif diff == Point(2, 0):
                t = Point(t.x - (1 if t.x > h.x else -1), t.y)
            elif diff == Point(0, 2):
                t = Point(t.x, t.y - (1 if t.y > h.y else -1))
            elif diff == Point(2, 1):
                t = Point(t.x - (1 if t.x > h.x else -1), h.y)
            elif diff == Point(1, 2):
                t = Point(h.x, t.y - (1 if t.y > h.y else -1))
            elif diff == Point(2, 2):
                t = Point(t.x - (1 if t.x > h.x else -1),
                          t.y - (1 if t.y > h.y else -1))

            rope[i] = h
            rope[i+1] = t

            travel.add(rope[-1])
        # print(dir, f"{step+1}/{dis}", list(enumerate(rope)))
        # print(m(rope))
        # print('#' * 30)

print(len(travel))
