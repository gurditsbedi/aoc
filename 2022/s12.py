from collections import namedtuple

Point = namedtuple('Point', 'x y')


class Point(Point):
    def __repr__(self):
        return f'({self.x}, {self.y})'


def valid_loc(shape, loc):
    return (0 <= loc.x < shape.x) and (0 <= loc.y < shape.y)


def m_get(m, p):
    return m[p.x][p.y]


def m_set(m, p, v):
    m[p.x][p.y] = v


f = open('in12.txt')
mat = [[ord(c) - ord('a') for c in line.strip()] for line in f]
shape = Point(len(mat), len(mat[0]))

start = None
end = None

done = 0
for j in range(shape.y):
    for i in range(shape.x):
        if mat[i][j] == ord('S') - ord('a'):
            mat[i][j] = ord('a') - ord('a')
            start = Point(i, j)
            done += 1
        if mat[i][j] == ord('E') - ord('a'):
            mat[i][j] = ord('z') - ord('a')
            end = Point(i, j)
            done += 1
        if done == 2:
            break
    if done == 2:
        break

directions = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]
visited = [[False for x in range(shape.y)] for y in range(shape.x)]
level = [[0 for x in range(shape.y)] for y in range(shape.x)]


Q = [start]
visited[start.x][start.y] = True
level[start.x][start.y] = 0


while Q:
    node = Q.pop(0)
    nv = m_get(mat, node)
    if node == end:
        break
    for d in directions:
        ngh_loc = Point(node.x+d.x, node.y+d.y)
        if not valid_loc(shape, ngh_loc):
            continue
        ngh = m_get(mat, ngh_loc)
        if not m_get(visited, ngh_loc):
            if (ngh - nv) <= 1:
                Q.append(ngh_loc)
                m_set(visited, ngh_loc, True)
                m_set(level, ngh_loc, m_get(level, node) + 1)

print(m_get(level, end))

# part 2

start = end

visited = [[False for x in range(shape.y)] for y in range(shape.x)]
level = [[0 for x in range(shape.y)] for y in range(shape.x)]


Q = [start]
visited[start.x][start.y] = True
level[start.x][start.y] = 0
while Q:
    node = Q.pop(0)
    nv = m_get(mat, node)
    for d in directions:
        ngh_loc = Point(node.x+d.x, node.y+d.y)
        if not valid_loc(shape, ngh_loc):
            continue
        ngh = m_get(mat, ngh_loc)
        if not m_get(visited, ngh_loc):
            if (nv - ngh) <= 1:
                Q.append(ngh_loc)
                m_set(visited, ngh_loc, True)
                m_set(level, ngh_loc, m_get(level, node) + 1)

smallest = (shape.x + 2) * (shape.y + 2)
for i in range(shape.x):
    for j in range(shape.y):
        if mat[i][j] == 0 and visited[i][j]:
            if level[i][j] < smallest:
                smallest = level[i][j]


print(smallest)
