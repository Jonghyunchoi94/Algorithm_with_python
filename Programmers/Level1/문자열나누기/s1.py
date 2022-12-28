s = "baaa"


def solution(s):
    answer = 0

    string = s[0]
    idx = 0
    store1 = 1
    store2 = 0

    if len(s) == 1:
        return 1

    for i in range(1, len(s)):
        if i == idx:
            if i == len(s) - 1:
                answer += 1
            continue

        if s[i] == string:
            store1 += 1
        else:
            store2 += 1

        if store1 != 0 and store2 != 0 and store1 == store2:
            store1, store2 = 1, 0
            answer += 1
            idx = i + 1
            if idx < len(s):
                string = s[idx]

    if store1 != 1 or store2 != 0:
        answer += 1

    return answer

print(solution(s))