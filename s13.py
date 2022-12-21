from functools import cmp_to_key
from json import loads as str_to_list


def compare(p1, p2):
    tp1, tp2 = type(p1), type(p2)

    if tp1 == int and tp2 == int:
        if p1 < p2:
            return 1
        elif p1 == p2:
            return 0
        elif p1 > p2:
            return -1

    elif tp1 == int and tp2 == list:
        return compare([p1], p2)

    elif tp1 == list and tp2 == int:
        return compare(p1, [p2])

    elif tp1 == list and tp2 == list:
        for x, y in zip(p1, p2):
            r = compare(x, y)
            if r != 0:
                return r

        if len(p1) < len(p2):
            return 1
        elif len(p1) == len(p2):
            return 0
        elif len(p1) > len(p2):
            return -1


f = open("in13.txt")
lines = [l.strip() for l in f]

packets = [[[2]], [[6]]]
sum_ = 0
for idx in range((len(lines) + 1) // 3):
    p1 = str_to_list(lines[3*idx])
    p2 = str_to_list(lines[3*idx+1])
    packets.append(p1)
    packets.append(p2)

    x = compare(p1, p2)
    if x == 1:
        sum_ += idx + 1


order = sorted(packets, key=cmp_to_key(lambda p1, p2: -compare(p1, p2)))
res = (order.index([[2]]) + 1) * (order.index([[6]])+1)
print(sum_)
print(res)
