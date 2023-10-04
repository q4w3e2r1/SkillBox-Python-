code = input()
sum_even_position = 0
sum_odd_position = 0
for i in range(len(code)):
    if (i+1) % 2 == 0:
        sum_even_position += int(code[i])
    else:
        sum_odd_position += int(code[i])
if (sum_odd_position + sum_even_position * 3) % 10 == 0:
    print('yes')
else:
    print('no')