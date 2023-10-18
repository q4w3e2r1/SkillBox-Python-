def euclid(maximum, minimum):
    if minimum == 0:
        return maximum
    else:
        return euclid(minimum, maximum % minimum)


maximum = int(input())
minimum = int(input())

print(maximum)