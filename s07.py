from dataclasses import dataclass


@dataclass
class Node:
    name: str
    size: int
    typee: str
    children: list


f = open('in07.txt', 'r')
lines = [x.strip() for x in f.readlines()]

root = Node('/', 0, 'd', [])
stack = [root]

i = 1
while i < len(lines):
    l = lines[i]
    if l.startswith('$'):
        _, command, *arg = [x.strip() for x in l.split()]
        if command == 'cd':
            if arg[0] == '..':
                stack.pop()
            else:
                for child in stack[-1].children:
                    if child.name == arg[0]:
                        current_node = child
                        break
                stack.append(current_node)
        elif command == 'ls':
            current_node = stack[-1]
            while i < len(lines)-1:
                i += 1
                currline = lines[i]
                if currline.startswith('$'):
                    i -= 1
                    break
                elif currline.startswith('dir'):
                    nd = Node(currline.split()[1], 0, 'd', [])
                    current_node.children.append(nd)
                else:
                    sz, name = currline.split()
                    nd = Node(name, int(sz), 'f', None)
                    current_node.children.append(nd)
    i += 1


def travel(root):
    if root.children is None:
        return root.size

    sz_sum = 0
    for child in root.children:
        sz_sum += travel(child)

    root.size = sz_sum
    return sz_sum


def travel_part1(root):
    if root.children is None:
        return 0

    sum_ = 0
    if root.size < 100000:
        sum_ += root.size

    for child in root.children:
        sum_ += travel_part1(child)

    return sum_


def travel_part2(root, req_space, current_best):
    best = current_best
    if req_space < root.size < best:
        best = root.size

    for child in root.children:
        if child.children is not None:
            t = travel_part2(child, req_space, best)
            if t < best:
                best = t

    return best


travel(root)
print(travel_part1(root))
req_space = 30000000 - (70000000 - root.size)
print(travel_part2(root, req_space, root.size))
