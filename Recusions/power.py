def power(n):
    if n == 0:
        return 1
    else:
        return 2 * power(n - 1)


print(power(10))
