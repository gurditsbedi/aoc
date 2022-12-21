f = open('in10.txt', 'r')

X = 1
cycle = 0
cv = [X]
for line in f.readlines():
    cmd, *args = line.strip().split()
    if cmd == 'addx':
        cv.append(X)
        cycle += 1

        X += int(args[0])

        cv.append(X)
        cycle += 1
    elif cmd == 'noop':
        cv.append(X)
        cycle += 1

print(cv[19::40])
print(sum(x * y for x, y in zip(range(20, 230, 40), cv[19::40])))

crt = [['.' for y in range(40)] for x in range(6)]
print('\n'.join(''.join(x) for x in crt))

for pos, x in enumerate(cv):
    pos_r = pos//40
    pos_c = pos % 40
    print(x, pos_r, pos_c)
    if abs(pos_c - x) < 2:
        crt[pos_r][pos_c] = '#'
    if pos > 1000:
        break

print('\n'.join(''.join(x) for x in crt))
