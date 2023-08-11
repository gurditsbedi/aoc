
def contains(x, y):
    # true if y is sub-range of x
    return (
        x[0] <= y[0] and y[1] <= x[1]
    )


def nonoverlap(x, y):
    return (x[1] < y[0]) or (y[1] < x[0])


f = open('in04.txt', 'r')
c = 0
c2 = 0
total_count = 0
for line in f.readlines():
    total_count += 1
    match = line.strip()
    er1, er2 = [tuple(int(y) for y in x.split('-')) for x in match.split(',')]
    c += (contains(er1, er2) or contains(er2, er1))
    c2 += nonoverlap(er1, er2)
print(c)
print(total_count - c2)
