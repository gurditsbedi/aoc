f = open('in02.txt', 'r')
v = dict(a=1, b=2, c=3)

# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
score = 0
mapper = dict(x='a', y='b', z='c')
for line in f.readlines():
    match = line.strip()
    op, mealias = [x.lower() for x in match.split(' ')]
    me = mapper[mealias]
    s = 0
    if op == me:
        s += 3
    elif f'{op}{me}' in 'abca':
        s += 6
    s += v[me]
    score += s

print(score)

# X lose, Y draw, and Z win.
f.seek(0)
score = 0
for line in f.readlines():
    match = line.strip()
    op, result = [x.lower() for x in match.split(' ')]
    s = 0

    if result == 'x':
        order = 'acba'
        choose = order[order.index(op)+1]
    if result == 'y':
        s += 3
        choose = op
    if result == 'z':
        s += 6
        order = 'abca'
        choose = order[order.index(op)+1]

    s += v[choose]
    score += s

print(score)
