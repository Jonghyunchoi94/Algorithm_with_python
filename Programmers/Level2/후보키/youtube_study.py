relation = [
    ["100","ryan","music","2"],["200","apeach","math","2"],
    ["300","tube","computer","3"],["400","con","computer","4"],
    ["500","muzi","music","3"],["600","apeach","music","2"]
]

from functools import cmp_to_key

def compare(a, b):
    x = bin(a).count('1')
    y = bin(b).count('1')
    return x - y

def check(relation, rowsize, colsize, subset):
    for a in range(rowsize - 1):
        for b in range(a + 1, rowsize):
            isSame = True
            for k in range(colsize):
                if (subset & 1 << k) == 0:
                    continue
                if relation[a][k] != relation[b][k]:
                    isSame = False
                    break
            if isSame:
                return False

    return True


def solution(relation):
    answer = 0
    rowsize = len(relation)
    colsize = len(relation[0])
    candidates = []

    for i in range(1, 1 << colsize):
        if check(relation, rowsize, colsize, i):
            # print("i: {}".format(i))
            candidates.append(i)
            # print("can: {}".format(candidates))

    candidates = sorted(candidates, key=cmp_to_key(compare))

    while len(candidates) != 0:
        n = candidates.pop(0)
        answer += 1
        candidates = [x for x in candidates if (n & x) != n]

    return answer

print(solution(relation))