import sys
sys.stdin = open('input.txt')

N = int(input())

map_data = [list(map(int, input())) for _ in range(N)]
check_data = [[0] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global cnt

    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]

        if 0 <= new_x < N and 0 <= new_y < N and map_data[new_x][new_y] == 1 and (new_x, new_y) not in visited:
            map_data[new_x][new_y] = 0
            visited.append((new_x, new_y))
            cnt += 1
            dfs(new_x, new_y)




house_cnt = []
visited = []
for i in range(len(map_data)):
    for j in range(len(map_data[i])):
        if map_data[i][j] == 1 and (i, j) not in visited:
            map_data[i][j] = 0
            cnt = 1
            visited.append((i, j))
            dfs(i, j)
            house_cnt.append(cnt)

house_cnt.sort()

print((len(house_cnt)))
for i in house_cnt:
    print(i)