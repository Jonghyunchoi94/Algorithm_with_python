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

    for l in range(len(lines)):
        D, S, T = lines[l].split()
        hour, minute, second = S.split(":")
        last = int(hour) * 3600 + int(minute) * 60 + float(second)

        temp = 0

        for nl in range(l, len(lines)):
            ND, NS, NT = lines[nl].split()
            nh, nm, ns = NS.split(":")
            nlast = int(nh) * 3600 + int(nm) * 60 + float(ns)
            term = float(NT.strip("s"))
            nstart = nlast - term + 0.001

            if last > nstart - 1:
                temp += 1

        answer = max(answer, temp)


    return answer

print(solution(lines))