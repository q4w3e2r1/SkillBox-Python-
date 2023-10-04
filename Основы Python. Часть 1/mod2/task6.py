text = input()
result = ""
for i in text:
    if i == '.':
        print(result)
        result = ""
    else:
        result += i
print(result)