n = 3
def generateParenthesis(n):
    res = []

    def dfs(open, close, string):
        nonlocal res
        if open < close or open > n:
            return

        if open == n and close == n:
            res.append(string)

        dfs(open+1, close, string + '(')
        dfs(open, close+1, string + ')')

    dfs(0, 0, '')


    return res

print(generateParenthesis(n))