import sys
sys.stdin = open('input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r, c, cnt, first_record):
    global ans, start_room

    if cnt >= ans:
        if cnt > ans:
            start_room = first_record
        else:
            if start_room > first_record:
                start_room = first_record
        ans = cnt

    for k in range(4):
        next_r = r + dr[k]
        next_c = c + dc[k]
        if 0 <= next_r < N and 0 <= next_c < N and room[next_r][next_c] == (room[r][c] + 1):
            visited.add((next_r, next_c))
            dfs(next_r, next_c, cnt + 1, first_record)
    return




T = int(input())

for case in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    ans = 1
    start_room = 987654321
    visited = set()
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited:
                visited.add((i, j))
                dfs(i, j, 1, room[i][j])
    print('#{} {} {}'.format(case + 1, start_room, ans))


