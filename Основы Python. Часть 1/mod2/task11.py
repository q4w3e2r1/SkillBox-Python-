sequence = input()
numbers = ''
result = False
for i in range(len(sequence)):
    if sequence[i] in numbers:
        result = True
        break
    if sequence[i] != ' ':
        numbers += sequence[i]

print(result)