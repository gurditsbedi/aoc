f = open('in05.txt', 'r')
rows = []
for line in f.readlines():
    l = line.rstrip()
    if not l:
        break
    # for n stacks, there are n*3 + (n-1) chars. vice-versa
    row = l[1::4]
    rows.append(row)

stacks = [[] for _ in range(len(rows[-1])+1)]
for row in reversed(rows[:-1]):
    for sno, el in enumerate(row, start=1):
        if el != ' ':
            stacks[sno].append(el)
stacks_copy = [x[:] for x in stacks]

f.seek(0)
for line in f.readlines():
    if not line.startswith('move'):
        continue
    l = line.strip()
    ins = [x for x in l.split()][1::2]
    movements, fr, to = [int(x) for x in ins]
    for _ in range(movements):
        x = stacks[fr].pop()
        stacks[to].append(x)

print(''.join(x[-1] for x in stacks[1:]))

stacks = stacks_copy
f.seek(0)
for line in f.readlines():
    if not line.startswith('move'):
        continue
    l = line.strip()
    ins = [x for x in l.split()][1::2]
    movements, fr, to = [int(x) for x in ins]
    tmpstack = []
    for _ in range(movements):
        x = stacks[fr].pop()
        tmpstack.append(x)
    for _ in range(movements):
        x = tmpstack.pop()
        stacks[to].append(x)

print(''.join(x[-1] for x in stacks[1:]))
