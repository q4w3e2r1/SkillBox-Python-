size = int(input())
matrix = list()
for i in range(size):
    matrix.append(list())
    for j in range(size):
        matrix[i].append(str(j + 1))
for i in range(size):
    print(", ".join(matrix[i]))
print()
for i in range(size):
    for j in range(i, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(size):
    print(", ".join(matrix[i]))