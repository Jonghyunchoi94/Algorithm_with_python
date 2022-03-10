import sys
sys.stdin = open('input.txt')


position = [input() for _ in range(5)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, y_cnt):
    global res
    if y_cnt > 3:
        return
    if cnt == 7:
        cur_path.append(visited)
        res += 1
        return

    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]

        if 0 <= next_x < 5 and 0 <= next_y < 5 and (next_x, next_y) not in visited:
            visited.add((next_x, next_y))
            if position[next_x][next_y] == 'S':
                dfs(next_x, next_y, cnt + 1, y_cnt)
            else:
                dfs(next_x, next_y, cnt + 1, y_cnt + 1)
            visited.remove((next_x, next_y))

res = 0
cur_path = []

for i in range(5):
    for j in range(5):
        visited = set()
        visited.add((i, j))
        if position[i][j] == 'S':
            dfs(i, j, 1, 0)
        else:
            dfs(i, j, 1, 1)

print(res)
print(cur_path)