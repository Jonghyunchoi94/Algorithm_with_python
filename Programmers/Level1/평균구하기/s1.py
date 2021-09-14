arr = [1,2,3,4]

def solution(arr):
    answer = 0
    cnt = 0
    for i in arr:
        answer += i
        cnt += 1
    answer /= cnt
    return answer

print(solution(arr))