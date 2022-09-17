orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

from collections import Counter

def solution(orders, course):
    answer = []
    res = []

    def dfs(word, length, n, s, visited):
        nonlocal answer
        if length == n:
            tmp = ""
            for idx in visited:
                tmp += word[idx]
            answer.append(tmp)
            return

        for i in range(s, len(word)):
            if visited[length] == 0:
                visited[length] = i
                dfs(word, length + 1, n, i + 1, visited)
                visited[length] = 0

    for c in course:
        answer = []
        for order in orders:
            if len(order) < c:
                continue
            visited = [0] * c
            dfs(sorted(order), 0, c, 0, visited)

        if answer:
            ans = Counter(answer)

        m = ans.most_common(1)[0][1]

        if m >= 2:
            for i in ans:
                if ans[i] == m:
                    res.append(i)

    return sorted(res)

print(solution(orders, course))