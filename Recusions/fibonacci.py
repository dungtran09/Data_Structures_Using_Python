def fib(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fib(n - 1)
        print("a=", a, "b=", b)
        return (a + b, a)


fib(6)
