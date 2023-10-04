information = input()
first = 0
second = 0
temp = ''
for i in information:
    if i == ',':
        first = int(temp)
        temp = ''
    if i != ' ' and i != ',':
        temp += i
second = int(temp)
print(first % second)