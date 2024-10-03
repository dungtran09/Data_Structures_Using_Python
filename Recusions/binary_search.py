def binary_search(S, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == S[mid]:
            return True
        elif target < S[mid]:
            return binary_search(S, target, low, mid - 1)
        else:
            return binary_search(S, target, mid + 1, high)


S = [1, 5, 6, 8, 10, 35, 46]
print(binary_search(S, 11, 0, len(S)))

