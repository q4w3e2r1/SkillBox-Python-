def check_he_winner(char):
    for i in range(k):
        flag = True
        for j in range(k):
            if playground[i][j] != char:
                flag = False
                break
        if flag:
            return True

    for i in range(k):
        flag = True
        for j in range(k):
            if playground[j][i] != char:
                flag = False
                break
        if flag:
            return True

    flag = True
    for j in range(k):
        if playground[j][j] != char:
            flag = False
            break
    if flag:
        return True

    flag = True
    for i in range(k):
        for j in range(k):
            if i + j == len(playground) - 1:
                if playground[j][i] != char:
                    flag = False
                    break
    if flag:
        return True

    return False


k = int(input())

playground = []

for i in range(k):
    playground.append(input())

if check_he_winner('X'):
    print('X')
elif check_he_winner('O'):
    print('O')
else:
    print("Ничья")

