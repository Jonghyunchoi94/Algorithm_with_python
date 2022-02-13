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
                if temp[1] in user_storage and temp[2] != user_storage[temp[1]]:
                    user_storage[temp[1]] = temp[2]
                    record_log.append((temp[1], 1))
                    answer.append("{}님이 들어왔습니다.".format(user_storage[temp[1]]))
                    for j in range(len(record_log)):
                        if record_log[j][0] == temp[1] and record_log[j][1] == 1:
                            answer[j] = "{}님이 들어왔습니다.".format(user_storage[temp[1]])
                        elif record_log[j][0] == temp[1] and record_log[j][1] == 2:
                            answer[j] = "{}님이 나갔습니다.".format(user_storage[temp[1]])
                else:
                    user_storage[temp[1]] = temp[2]
                    record_log.append((temp[1], 1))
                    answer.append("{}님이 들어왔습니다.".format(user_storage[temp[1]]))
            elif temp[0] == "Change":
                user_storage[temp[1]] = temp[2]
                for j in range(len(record_log)):
                    if record_log[j][0] == temp[1] and record_log[j][1] == 1:
                        answer[j] = "{}님이 들어왔습니다.".format(user_storage[temp[1]])
                    elif record_log[j][0] == temp[1] and record_log[j][1] == 2:
                        answer[j] = "{}님이 나갔습니다.".format(user_storage[temp[1]])

        elif len(temp) == 2:
            record_log.append((temp[1], 2))
            answer.append("{}님이 나갔습니다.".format(user_storage[temp[1]]))


    return answer

print(solution(record))