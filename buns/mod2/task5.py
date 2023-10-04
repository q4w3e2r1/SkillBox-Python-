text = input()
start = text[0]
distance = ''

for i in range(len(text)):
    if text[i] != ',' and i != 0:
     distance += text[i]

distance = int(distance)

print(chr((ord(start) - 97 + distance) % 26 + 97))