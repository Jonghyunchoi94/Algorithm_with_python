import sys
sys.stdin = open('input.txt')


dr = [-1,1,0,0]
dc = [0,0,1,-1]

def dfs(r, c, num):
    global number
    if num == 7:
        visited.add(number)
        return

    for k in range(4):
        next_r = r + dr[k]
        next_c = c + dc[k]
        if 0 <= next_r < 4 and 0 <= next_c < 4:
            number += data[r][c]
            dfs(next_r, next_c, num + 1)
            number = number[:-1]


T = int(input())

for case in range(T):
    data = [list(input().split()) for _ in range(4)]
    number = ''
    visited = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j ,0)
    print('#{} {}'.format(case + 1, len(visited)))