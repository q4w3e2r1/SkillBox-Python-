s = input()
counter = 0
for i in s:
    if i == '1':
        counter += 1
    else:
        counter -= 1
if counter == 0:
    print("yes")
else:
    print('no')