import sys
sys.stdin = open('input.txt')

def pos(array1, array2):
    global honey, answer
    answer = []
    dfs(0, 0, 0, array1)
    max_array1 = max(answer)
    answer = []
    dfs(0, 0, 0, array2)
    max_array2 = max(answer)

    if max_array1 + max_array2 > honey:
        honey = max_array1 + max_array2

def dfs(num, result, res, arr):
    if res > C:
        return

    if num == M:
        if res <= C:
            answer.append(result)
        return

    dfs(num + 1, result, res, arr)
    dfs(num + 1, result + (arr[num] ** 2), res + arr[num], arr)


# array1, array2 구하기
def start_point(r, c):
    # 같은 행
    for i in range(c + M, N - M + 1):
        pos(data[r][c:c + M], data[r][c + M:c + (2 * M)])

    # 다른 행
    for i in range(r + 1, N):
        for j in range(N - M + 1):
            pos(data[r][c:c + M], data[i][j:j + M])

T = int(input())

for case in range(T):
    N, M, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    honey = -987654321
    for i in range(N):
        for j in range(N - M + 1):
            start_point(i, j)

    print('#{} {}'.format(case + 1, honey))

