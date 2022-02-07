"""
요금표
기본시간 : 180분
기본요금 : 5000원
단위시간 : 10분
단위요금 : 600원
"""

fees = 	[1, 461, 1, 10]
records = [
    "00:00 1234 IN"
]

def solution(fees, records):
    answer = {}
    storage = {}
    for i in records:
        time, num, status = i.split()
        hour, minute = time.split(":")
        time_val = int(hour) * 60 + int(minute)
        # 처음 입차
        if num not in storage:
            storage[num] = time_val
        elif status == "IN":
            storage[num] = time_val
        elif status == "OUT":
            if num not in answer:
                answer[num] = time_val - storage[num]
            else:
                answer[num] += (time_val - storage[num])
            storage[num] = -1

    # 23: 59
    last_time = 23 * 60 + 59
    for i, j in storage.items():
        if j != -1:
            if i not in answer:
                answer[i] = last_time - storage[i]
            else:
                answer[i] += last_time - storage[i]

    # 요금 변환
    for k, v in answer.items():
        if v <= fees[0]:
            answer[k] = fees[1]
        else:
            if (v - fees[0]) % fees[2]:
                answer[k] = fees[1] + ((((v - fees[0])//fees[2]) + 1) * fees[3])
            else:
                answer[k] = fees[1] + (((v - fees[0])//fees[2]) * fees[3])

    ans = sorted(answer.items(), key=lambda x:x[0])
    res = []
    for i, j in ans:
        res.append(j)
    return res

print(solution(fees, records))