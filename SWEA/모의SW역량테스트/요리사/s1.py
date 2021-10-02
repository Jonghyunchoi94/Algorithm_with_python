import sys
sys.stdin = open('input.txt')

def dfs(num, s):
    if num == N // 2:
        res = visited[:]
        com_food.append(res)
        return

    for i in range(s, N):
        visited[num] = i
        dfs(num + 1, i + 1)

def combi(data):
    res = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            res += food[data[i]][data[j]]
            res += food[data[j]][data[i]]
    return res



T = int(input())

for case in range(T):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N // 2)
    com_food = []
    dfs(0, 0)
    ans = 987654321
    for k in range(len(com_food)//2):
        food_a = 0
        food_b = 0
        food_a += combi(com_food[k])
        food_b += combi(com_food[len(com_food) - 1 - k])
        if ans > abs(food_a - food_b):
            ans = abs(food_a - food_b)
    print('#{} {}'.format(case + 1, ans))