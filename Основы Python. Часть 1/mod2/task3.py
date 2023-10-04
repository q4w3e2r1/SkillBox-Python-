def main():
    information = input()
    count_separator = 0
    first = ''
    second = ''
    third = ''
    for i in information:
        if i == ' ':
            count_separator += 1
        if count_separator == 0:
            first += i
        if count_separator == 1:
            second += i
        if count_separator == 2:
            third += i
    first, second, third = int(first), int(second), int(third)
    print(first + second + third - find_max(first, second, third) - find_min(first, second, third))


def find_max(first, second, third):
    if first > second and first > third:
        return first
    if second > first and second > third:
        return second
    return third


def find_min(first, second, third):
    if first < second and first < third:
        return first
    if second < first and second < third:
        return second
    return third


main()
