lines =  [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]

def solution(lines):
    answer = 0
    f_start = 987654321
    total = 24 * 3600 * 1000
    confirm = [0] * total
    for line in lines:
        D, S, T = line.split()
        hour, minute, second = S.split(":")
        last = (int(hour) * 3600 + int(minute) * 60 + float(second))
        term = T.strip("s")
        start = last - float(term) + 0.001
        nlast = int(last * 1000)
        nstart = int(start * 1000)
        f_start = min(f_start, nstart)
        confirm[nstart] += 1
        confirm[nlast] -= 1

    for i in range(f_start, nlast + 1):
        confirm[i + 1] += confirm[i]
    print(confirm[f_start: nlast + 1])

    return max(confirm)

print(solution(lines))