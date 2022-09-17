play_time = "99:59:59"
adv_time = "25:00:00"
logs = [
    "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59",
    "11:00:00-31:00:00"
]

def solution(play_time, adv_time, logs):
    h, m, s = play_time.split(":")
    pt = 3600 * int(h) + 60 * int(m) + int(s)

    record = [0] * (pt + 1)

    for log in logs:
        start, end = log.split("-")
        h1, m1, s1 = start.split(":")
        h2, m2, s2 = end.split(":")
        pt1 = 3600 * int(h1) + 60 * int(m1) + int(s1)
        pt2 = 3600 * int(h2) + 60 * int(m2) + int(s2)

        record[pt1] += 1
        record[pt2] -= 1

    for i in range(len(record) - 1):
        record[i + 1] += record[i]

    for i in range(len(record) - 1):
        record[i + 1] += record[i]

    hr, mr, sr = adv_time.split(":")
    ptr = 3600 * int(hr) + 60 * int(mr) + int(sr)

    ans = 0
    res = 0
    for i in range(ptr - 1, len(record)):
        if i >= ptr:
            if record[i] - record[i - ptr] > ans:
                ans = record[i] - record[i - ptr]
                res = i - ptr + 1
        else:
            if record[i] > ans:
                ans = record[i]
                res = i - ptr + 1

    hp, mp, sp = str(res // 3600), str((res % 3600) // 60), str((res % 3600) % 60)

    if len(hp) == 1:
        hp = "0" + hp
    if len(mp) == 1:
        mp = "0" + mp
    if len(sp) == 1:
        sp = "0" + sp

    r = [hp, mp, sp]
    answer = ":".join(r)


    return answer

print(solution(play_time, adv_time, logs))