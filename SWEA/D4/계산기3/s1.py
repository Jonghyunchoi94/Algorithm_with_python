import sys
sys.stdin = open('input.txt')

"""
“3+(4+5)*6+7” -> "345+6*+7+"
"""


for testcase in range(10):
    N = int(input())
    T = input()

    bracket_cal = []

    stack = []

    for i in range(len(T)):
        if T[i] == "(":
            bracket_cal.append(T[i])
        elif T[i] == "+":
            while bracket_cal:
                tmp = bracket_cal[-1]
                if tmp == "(":
                    break
                else:
                    stack.append(bracket_cal.pop())
            bracket_cal.append(T[i])
        elif T[i] == "*":
            while bracket_cal:
                tmp = bracket_cal[-1]
                if tmp == "(" or tmp == "+":
                    break
                else:
                    stack.append(bracket_cal.pop())
            bracket_cal.append(T[i])
        elif T[i] == ")":
            while bracket_cal:
                tmp = bracket_cal.pop()
                if tmp == "(":
                    break
                else:
                    stack.append(tmp)
        else:
            stack.append(T[i])
    while bracket_cal:
        tmp = bracket_cal.pop()
        stack.append(tmp)

    num = []
    res = 0
    for i in stack:
        if i == "*" or i == "+":
            tmp1 = num.pop()
            tmp2 = num.pop()

            if i == "*":
                num.append(tmp1 * tmp2)
            else:
                num.append(tmp1 + tmp2)
        else:
            num.append(int(i))

    res = num[0]

    print("#{} {}".format(testcase + 1, res))
