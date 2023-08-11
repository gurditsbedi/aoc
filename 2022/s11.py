from dataclasses import dataclass


@dataclass
class Monkey:
    idx: int
    levels: list[int]
    operation: list[str]
    test: int
    test_true: int
    test_false: int


f = open('in11.txt', 'r')
lines = [x.strip() for x in f.readlines()]
monkeys = []
for i in range(len(lines)//6):
    idx = 7 * i
    m_id = int(lines[idx].split()[-1][:-1])
    items = [int(x.strip()) for x in lines[idx+1].split(':')[1].split(',')]
    operation = [x.strip() for x in lines[idx+2].split('=')[1].split()]
    test = int(lines[idx+3].split()[-1])
    test_true = int(lines[idx+4].split()[-1])
    test_false = int(lines[idx+5].split()[-1])
    mky = Monkey(m_id, items, operation, test, test_true, test_false)
    monkeys.append(mky)
    if m_id == 7:
        break


def evaluate_operation(value, operation):
    x, operator, y = operation
    x = value if x == 'old' else int(x)
    y = value if y == 'old' else int(y)
    if operator == '+':
        return x + y
    elif operator == '*':
        return x * y


def f(rounds, reducer, part):
    inspect = [0 for _ in monkeys]
    for r in range(rounds):
        for monkey in monkeys:
            for i in range(len(monkey.levels)):
                inspect[monkey.idx] += 1
                item = monkey.levels.pop(0)

                new_item = evaluate_operation(item, monkey.operation)
                if part == 1:
                    new_item = new_item // 3
                elif part == 2:
                    new_item = new_item % reducer

                if new_item % monkey.test == 0:
                    monkeys[monkey.test_true].levels.append(new_item)
                else:
                    monkeys[monkey.test_false].levels.append(new_item)

    m = max(inspect)
    m2 = max(x for x in inspect if x != m)
    return m * m2


product = 1
for m in monkeys:
    product *= m.test

print(f(20, 3, 1))
print(f(10**4, product, 2))
