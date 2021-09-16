arr = [4,3,2,1]

def solution(arr):
    min_val = 987654321
    idx = 0
    for i, j in enumerate(arr):
        if j < min_val:
            min_val = j
            idx = i
    arr.pop(idx)

    if arr:
        return arr
    else:
        return [-1]


print(solution(arr))