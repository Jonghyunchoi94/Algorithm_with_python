places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

def solution(places):
    answer = []
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    def dfs(road, r, c, length):
        nonlocal Flag
        if length > 2:
            return

        if length > 0 and road[r][c] == "P":
            Flag = True
            return

        if road[r][c] == "X":
            return

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) not in visited:
                visited.add((nr, nc))
                dfs(road, nr, nc, length + 1)
                visited.remove((nr, nc))

        return

    for place in places:
        Flag = False
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P":
                    visited = set()
                    visited.add((r, c))
                    dfs(place, r, c, 0)
                if Flag:
                    break
            if Flag:
                break

        if Flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer

print(solution(places))