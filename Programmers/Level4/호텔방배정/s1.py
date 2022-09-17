k = 10
room_number = [1,3,4,1,3,1]

from collections import defaultdict

def solution(k, room_number):
    answer = []
    # 방 배정 현황
    room = [False] * (k + 1)

    # 연결리스트 사용
    storage = defaultdict(list)

    for i in range(1, k + 1):
        storage[i] = [i - 1, i + 1]


    for n in room_number:
        cursor = n
        if not cursor:
            room[cursor] = True
            answer.append(cursor)
        else:

        while room[cursor]:
            cursor = storage[cursor][1]
        room[cursor] = True
        answer.append(cursor)

    return answer

print(solution(k, room_number))
