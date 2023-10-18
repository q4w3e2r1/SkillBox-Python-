def raising_degree(a, n):
    if n < 0:
        return 1 / raising_degree(a, -n)
    if n == 0:
        return 1
    elif n % 2 == 0:
        return raising_degree(a**2, n // 2)
    else:
        return a * raising_degree(a, n-1)


print(raising_degree(3, -1))