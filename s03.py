def priority(alpha):
    o = ord(alpha)
    if ord('a') <= o <= ord('z'):
        return o - ord('a') + 1
    else:
        return 26 + o - ord('A') + 1


f = open('in03.txt', 'r')
s = 0
for line in f.readlines():
    match = line.strip()
    l = len(match)//2
    x = set(match[:l])
    y = set(match[l:])
    c = list(x & y)[0]

    s += priority(c)
print(s)

f.seek(0)
s = 0
i = 0
gr = []
for line in f.readlines():
    match = line.strip()
    gr.append(match)
    i += 1
    if i % 3 == 0:
        x, y, z = [set(x) for x in gr]
        c = list(x & y & z)[0]
        s += priority(c)
        gr = []


print(s)
