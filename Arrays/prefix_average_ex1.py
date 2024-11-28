def prefix_average(S):
    n = len(S)
    A = [0] * n
    total = 0
    for i in range(n):
        total += S[i]
        A[i] = total / (i + 1)

    return A


S = [1, 2, 3, 4, 5]


A = prefix_average(S)

print(A)
