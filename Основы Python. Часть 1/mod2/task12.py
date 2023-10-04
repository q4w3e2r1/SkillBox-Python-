phone_number = input()
result = ''
for i in phone_number:
    if i != ')' and i != '(' and i != '-' and i != ' ':
        result += i
print(result)