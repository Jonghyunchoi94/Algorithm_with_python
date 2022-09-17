n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]


def solution(n, info):
    res = 0
    pos = 11
    answer = [0] * len(info)
    visited = [0] * len(info)
    fin = [0] * len(info)

    appeach = 0
    for i in range(len(info)):
        if info[i] != 0:
            appeach += (10 - i)

    def dfs(n, r_score, a_score, f_score):
        nonlocal res, pos, fin
        if n < 0:
            return

        if n == 0:
            if (r_score - a_score) > res:
                pos = f_score
                res = (r_score - a_score)
                fin = [i for i in answer]

            elif (r_score - a_score) == res:
                if f_score < pos:
                    pos = f_score
                    fin = [i for i in answer]

            return


        for i in range(len(info)):
            if visited[i] == 0:
                visited[i] = 1
                if info[i] + 1 <= n:
                    answer[i] = info[i] + 1
                    tmp = 10 - i
                else:
                    answer[i] = n
                    tmp = 0
                if info[i] == 0:
                    dfs(n - answer[i], r_score + tmp, a_score, 10 - i)
                else:
                    dfs(n - answer[i], r_score + tmp, a_score - tmp, 10 - i)
                answer[i] = 0
                visited[i] = 0

        return

    dfs(n, 0, appeach, 10)

    if res == 0:
        return [-1]
    else:
        return fin

print(solution(n, info))