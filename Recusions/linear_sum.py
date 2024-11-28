def sum(S, n):
    if n == 0:
        return 0
    else:
        return sum(S, n - 1) + S[n - 1]


S = [1, 2, 3, 4]

print(sum(S, S.__len__()))
