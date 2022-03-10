import sys
sys.stdin = open('input.txt')

"""
갈래길을 둘 다 선택해야 할 수 있다. 
좌표로 dfs로 하는 것이 아니라 박스 번호를 매겨 해결해야한다.
"""

position = [input() for _ in range(5)]
cur_person = []
visited = set()
res = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def check(num):
    global possible
    r = num // 5
    c = num % 5

    for k in range(4):
        next_r = r + dr[k]
        next_c = c + dc[k]

        if 0 <= next_r < 5 and 0 <= next_c < 5 and (next_r, next_c) not in visited:
            nextNum = next_r * 5 + next_c
            if nextNum in cur_person:
                visited.add((next_r, next_c))
                possible += 1
                check(nextNum)



def dfs(person, y_cnt, box):
    global res, possible, visited
    if y_cnt > 3 or 25 - box < 7 - person:
        return

    if person == 7:
        possible = 1
        visited = set()
        visited.add((cur_person[0] // 5, cur_person[0] % 5))
        check(cur_person[0])
        if possible == 7:
            res += 1
        return

    r = box // 5
    c = box % 5

    # 해당 박스 번호 사용
    if position[r][c] == 'Y':
        cur_person.append(box)
        dfs(person + 1, y_cnt + 1, box + 1)
        cur_person.pop()
    else:
        cur_person.append(box)
        dfs(person + 1, y_cnt, box + 1)
        cur_person.pop()

    # 해당 박스 번호 사용하지 않음
    dfs(person, y_cnt, box + 1)

dfs(0, 0, 0)
print(res)