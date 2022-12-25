data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3


def solution(data, col, row_begin, row_end):
    answer = 0

    sorted_data = sorted(data, key=lambda x:(x[col - 1], -x[0]))


    for i in range(row_begin - 1, row_end):
        temp = 0
        for j in sorted_data[i]:
            temp += j % (i + 1)
        answer ^= temp

    return answer

print(solution(data, col, row_begin, row_end))
