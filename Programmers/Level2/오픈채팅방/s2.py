record = [
    "Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
    "Enter uid1234 Prodo","Change uid4567 Ryan"
]

"""
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.",
 "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
"""


def solution(record):
    answer = []

    user_storage = {}
    record_log = []

    for i in record:
        temp = i.split()
        if len(temp) == 3:
            if temp[0] == "Enter":
                user_storage[temp[1]] = temp[2]
                record_log.append((temp[1], 1))
            elif temp[0] == "Change":
                user_storage[temp[1]] = temp[2]
        elif len(temp) == 2:
            record_log.append((temp[1], 2))

    for ip, action in record_log:
        if action == 1:
            answer.append("{}님이 들어왔습니다.".format(user_storage[ip]))
        else:
            answer.append("{}님이 나갔습니다.".format(user_storage[ip]))
    return answer

print(solution(record))