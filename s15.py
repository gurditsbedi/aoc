
from collections import namedtuple
import re

Point = namedtuple('Point', 'x y')


class Point(Point):
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def mdist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


cases = [dict(fname="in15s.txt", reqrow=10),
         dict(fname="in15.txt", reqrow=2000000)]

case = 1
f = open(cases[case]['fname'])
reqrow = cases[case]['reqrow']
pairs = []
for l in f:
    words = l.strip().split()
    s = (int(words[2][2:-1]), int(words[3][2:-1]))
    b = (int(words[8][2:-1]), int(words[9][2:]))
    pairs.append((Point(*s), Point(*b)))

# part 1
reqrow_search_ranges = []
for s, b in pairs:
    md = s.mdist(b)

    search_intersects = s.y - md <= reqrow <= s.y + md

    if search_intersects:
        one_side_width = md - abs(reqrow - s.y)
        reqrow_search_ranges.append((s.x-one_side_width, s.x+one_side_width))


# merge intervals
reqrow_search_ranges.sort()
for i in range(1, len(reqrow_search_ranges)):
    r1, r2 = reqrow_search_ranges[i-1], reqrow_search_ranges[i]
    if r1[1] >= r2[0]:
        newr = (r1[0], max(r1[1], r2[1]))
        reqrow_search_ranges[i] = newr
        reqrow_search_ranges[i-1] = None


on_row_s = sum(1 for s, _ in pairs if s.y == reqrow)
on_row_b = len(set(b for _, b in pairs if b.y == reqrow))
on_row_sb = on_row_s + on_row_b

count = sum(
    x[1]-x[0]+1 for x in reqrow_search_ranges if x is not None) - on_row_sb
print(count)

# part 2
