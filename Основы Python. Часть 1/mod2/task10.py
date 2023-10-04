words = input()
result = ''
for i in range(len(words)):
    if words[i] == ' ':
        result += words[i - 1]
result += words[-1]
print(result)