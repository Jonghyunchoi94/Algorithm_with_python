arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]


def inner_product(list1, list2):
    res = 0
    for i in range(len(list1)):
        res += list1[i] * list2[i]
    return res


def solution(arr1, arr2):
    answer = []
    zip_arr2 = list(zip(*arr2))
    for i in range(len(arr1)):
        plus = []
        for j in range(len(zip_arr2)):
            plus.append(inner_product(arr1[i], zip_arr2[j]))
        answer.append(plus)
    return answer

print(solution(arr1, arr2))