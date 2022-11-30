p = "))))(((("


def balancestr(p):
    n1 = 0
    n2 = 0
    for i in range(len(p)):
        if p[i] == "(":
            n1 += 1
        else:
            n2 += 1
    if n1 == n2:
        return True
    else:
        return False

def rightstr(p):
    stack = []
    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        elif p[i] == ")":
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True

def reverse(p):
    answer = ""
    for i in range(len(p)):
        if p[i] == "(":
            answer += ")"
        else:
            answer += "("
    return answer

def seperate(p):
    if p == "":
        return ""

    u = ""
    v = ""
    Flag = False
    for i in range(len(p)):
        if Flag:
            v += p[i]
        else:
            u += p[i]
        if balancestr(u):
            Flag = True

    if rightstr(u):
        return u + seperate(v)
    else:
        return "(" + seperate(v) + ")" + reverse(u[1:-1])


def solution(p):
    answer = seperate(p)

    if rightstr(p):
        return p

    return answer

print(solution(p))