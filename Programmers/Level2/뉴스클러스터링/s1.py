str1 = "FRANCE"
str2 = "french"

from collections import defaultdict

def solution(str1, str2):
    storage = defaultdict(list)

    for i in range(len(str1) - 1):
        temp = str1[i: i + 2]

        if temp.isalpha():
            temp = temp.lower()
            if temp not in storage:
                storage[temp].extend([1, 0])
            else:
                storage[temp][0] += 1

    for i in range(len(str2) - 1):
        temp = str2[i: i + 2]

        if temp.isalpha():
            temp = temp.lower()
            if temp not in storage:
                storage[temp].extend([0, 1])
            else:
                storage[temp][1] += 1

    numerator = sum([min(storage[i][0],storage[i][1]) for i in storage])
    denominator = sum([max(storage[i][0],storage[i][1]) for i in storage])

    if numerator == 0 and denominator == 0:
        similarity = 1 * 65536
    else:
        similarity = int(numerator / denominator * 65536)

    return similarity

print(solution(str1, str2))