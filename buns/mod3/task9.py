file = open("input.txt", "r")
n = int(file.read())
file.close()
x, y = 0, 0
sideNum = 1
sideLength = 1
i = 0
dx, dy = 1, 1
while n > i:
    dx, dy = -dx, -dy
    for j in range(sideLength):
        x += dx
        i += 1
        if i == n:
            dx, dy = 0, 0
            break
    for j in range(sideLength):
        y += dy
        i += 1
        if i == n:
            dx, dy = 0, 0
            break
    sideLength += 1
file = open("output.txt", "w")
file.write(x, y)
file.close()