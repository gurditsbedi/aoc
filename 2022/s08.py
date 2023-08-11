from itertools import zip_longest


def l2r(matrix, visibility):
    for i in range(1, len(matrix)-1):
        row = matrix[i]
        visrow = visibility[i]
        large = row[0]
        for i, el in enumerate(row):
            if el > large:
                visrow[i] = 1
                large = el

        large = row[-1]
        for i, el in enumerate(reversed(row)):
            if el > large:
                visrow[len(row) - i-1] = 1
                large = el


def transpose(l):
    return list(map(list, zip_longest(*l, fillvalue=None)))


fname = 'in08.txt'
lines = [x.strip() for x in open(fname, 'r').readlines()]

matrix = []
for line in lines:
    row = [int(x) for x in list(line)]
    matrix.append(row)

visibility = [[0 for x in lines] for y in lines]
for i in range(len(lines)):
    for j in range(len(lines)):
        if i in (0, len(lines) - 1) or j in (0, len(lines) - 1):
            visibility[i][j] = 1

l2r(matrix, visibility)
matrix = transpose(matrix)
visibility = transpose(visibility)
l2r(matrix, visibility)

# print(sum(sum(x) for x in visibility))

matrix = transpose(matrix)
visibility = transpose(visibility)

# print(matrix)
# print(visibility)

res = 0

for i in range(1, len(matrix)-1):
    for j in range(1, len(matrix[i])-1):

        left = 0
        for k in range(j-1, -1, -1):
            left += 1
            if matrix[i][k] >= matrix[i][j]:
                break

        right = 0
        for k in range(j+1, len(matrix[i])):
            right += 1
            if matrix[i][k] >= matrix[i][j]:
                break

        up = 0
        for k in range(i-1, -1, -1):
            up += 1
            if matrix[k][j] >= matrix[i][j]:
                break

        down = 0
        for k in range(i+1, len(matrix)):
            down += 1
            if matrix[k][j] >= matrix[i][j]:
                break

        new = left * right * up * down
        if new > res:
            res = new
print(res)
