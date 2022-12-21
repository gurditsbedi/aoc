
f = open('in01.txt', 'r')
g = []
s = 0
for line in f.readlines():
    x = line.strip()
    if x:
        s += int(x)
    else:
        g.append(s)
        s = 0
print(max(g))
print(sum(sorted(g)[-3:]))
