def unique1(S):
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                print("The list is Duplicated")
                return

    print("The list is Unique")
    return


S = [1, 3, 5, 7, 9, 9]

unique1(S)
