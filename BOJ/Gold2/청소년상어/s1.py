import sys
sys.stdin = open('input.txt')

"""
첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다. 
물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다. 
방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 
의미한다.
"""

from copy import deepcopy

mapdata = [[0] * 4 for _ in range(4)]
direction = {}
where = {}

for row in range(4):
    data = list(map(int, input().split()))
    for i, j in enumerate(data):
        if i % 2 == 0:
            mapdata[row][i//2] = j
            where[j] = [row, i//2]
        else:
            direction[data[i-1]] = j


shark = []

dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]


shark.append(mapdata[0][0])
change_map = deepcopy(mapdata)
ans = 0

def move_fish(change_map, direction, where, shark):
    new_change_map = deepcopy(change_map)
    new_direction = deepcopy(direction)
    new_where = deepcopy(where)
    new_shark = deepcopy(shark)
    for i in range(1, 17):
        if i not in new_shark:
            tmp = new_direction[i]
            cnt = 0
            while True:
                if tmp == 9:
                    tmp = 1
                if cnt == 8:
                    break

                next_x = new_where[i][0] + dx[tmp]
                next_y = new_where[i][1] + dy[tmp]

                if (not (0 <= next_x < 4)) or (not (0 <= next_y < 4)) or (new_change_map[next_x][next_y] == shark[-1]):
                    cnt += 1
                    tmp += 1
                    continue

                if 0 <= next_x < 4 and 0 <= next_y < 4:
                    cur = new_change_map[new_where[i][0]][new_where[i][1]]
                    cur_map = [new_where[i][0], new_where[i][1]]
                    val = new_change_map[next_x][next_y]
                    val_map = [next_x, next_y]

                    new_change_map[new_where[i][0]][new_where[i][1]] = val
                    new_change_map[next_x][next_y] = cur

                    new_where[cur] = val_map
                    new_where[val] = cur_map

                    new_direction[i] = tmp
                    break

    return new_change_map, new_direction, new_where, new_shark


# print(change_map)
# print(direction)
# print(where)


def move_shark(change_map, direction, where, shark):
    x, y = where[shark[-1]]
    d = direction[shark[-1]]

    possible = []
    k = 1
    while True:
        next_x = x + (dx[d] * k)
        next_y = y + (dy[d] * k)

        if (not (0 <= next_x < 4)) or (not (0 <= next_y < 4)):
            break

        if 0 <= next_x < 4 and 0 <= next_y < 4 and change_map[next_x][next_y] not in shark:
            possible.append(change_map[next_x][next_y])

        k += 1
    return possible

def dfs(change_map, direction, where, shark):
    global ans
    new_change_map, new_direction, new_where, new_shark = move_fish(change_map, direction, where, shark)
    possible = move_shark(new_change_map, new_direction, new_where, new_shark)

    if not possible:
        ans = max(ans, sum(new_shark))
        return

    for i in possible:
        new_shark.append(i)
        dfs(new_change_map, new_direction, new_where, new_shark)
        new_shark.pop()


dfs(change_map, direction, where, shark)

print(ans)