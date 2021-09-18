n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    lost = set(lost)
    reserve = set(reserve)
    lost_r = lost - reserve
    reserve_r = reserve - lost
    for i in lost_r:
        if (i - 1) in reserve_r:
            answer += 1
            reserve_r.remove(i - 1)
            continue
        elif (i + 1) in reserve_r:
            answer += 1
            reserve_r.remove(i + 1)
            continue
    answer = n - (len(lost_r) - answer)
    return answer

print(solution(n, lost, reserve))