text = input()
char = text[-1]
s = text[:-2]
counter = 0
for i in range(len(s)):
    if s[i] == char:
        counter += 1
    else:
        break
print(counter)