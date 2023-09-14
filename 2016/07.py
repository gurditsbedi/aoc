def checker(s):
    return s[0] != s[1] and s[1] == s[2] and s[0] == s[3]


def window(s, w=4):
    for i in range(len(s) - w + 1):
        yield s[i : i + w]


def part1(x):
    # print(x)
    a = [w for word in x[::2] for w in window(word)]
    b = [w for word in x[1::2] for w in window(word)]
    ca = map(checker, a)
    cb = map(lambda x: not checker(x), b)
    return any(ca) * all(cb)


def part2(x):
    a = [w for word in x[::2] for w in window(word, w=3)]
    b = [w for word in x[1::2] for w in window(word, w=3)]

    def compare(x, y):
        return (
            x[0] != x[1]
            and y[0] != y[1]
            and x[0] == y[1]
            and y[1] == x[2]
            and y[0] == x[1]
            and x[1] == y[2]
        )

    for x in a:
        for y in b:
            if compare(x, y):
                return 1

    return 0


f = open("i/07")

inp_parsed = [
    [s for part in l.strip().split("[") for s in part.split("]")] for l in f.readlines()
]

a1 = sum(part1(line) for line in inp_parsed)
a2 = sum(part2(line) for line in inp_parsed)
print(a1)
print(a2)
