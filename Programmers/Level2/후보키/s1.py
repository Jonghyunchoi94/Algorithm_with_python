relation = [
    ["100","ryan","music","2"],["200","apeach","math","2"],
    ["300","tube","computer","3"],["400","con","computer","4"],
    ["500","muzi","music","3"],["600","apeach","music","2"]
]
"""
후보키의 개념

1. 유일성
2. 최소성

표현
0. 칼럼명이 없다 -> 칼럼 인덱스를 붙임


"""

# 유일성 만족
def unique_condition(data, input_str):
    rec = []
    for i in range(len(data)):
        tmp = ''
        for j in input_str:
            tmp += data[i][int(j)]

        if tmp in rec:
            return False
        else:
            rec.append(tmp)

    return True

def dfs(idx, data, str, n):
    global storage
    if idx == n:
        storage.append(str)
        return

    dfs(idx + 1, data, str, n)
    dfs(idx + 1, data, str + data[idx], n)

def solution(relation):
    global storage
    n = len(list(zip(*relation)))
    tot_str = "".join(map(str, range(n)))
    storage = []
    unique = []
    minimum = []
    dfs(0, tot_str, "", n)

    storage.sort()

    # 유일성 만족
    for i in storage:
        if unique_condition(relation, i):
            unique.append(i)
    unique.sort(key = lambda x: len(x))
    # 최소성 만족
    for i in unique:
        storage = []
        dfs(0, i, '', len(i))
        # print(i)
        # print(storage)
        for j in storage:
            if j == '':
                continue
            if j in minimum:
                break
        else:
            minimum.append(i)

    return len(minimum)

print(solution(relation))