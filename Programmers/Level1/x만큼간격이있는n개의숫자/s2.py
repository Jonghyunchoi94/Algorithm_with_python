def solution(x, n):
    return [i * x + x for i in range(n)]
print(solution(2, 5))