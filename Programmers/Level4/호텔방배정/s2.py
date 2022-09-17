import sys
sys.setrecursionlimit(10000)

k = 10
room_number = [1,3,4,1,3,1]

def emptyRoom(number, rooms):
    if number not in rooms:
        rooms[number] = number + 1
        return number
    empty = emptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty

def solution(k, room_number):
    answer = []
    rooms = dict()

    for num in room_number:
        emptyRoomNumber = emptyRoom(num, rooms)
        answer.append(emptyRoomNumber)
    return answer

print(solution(k, room_number))