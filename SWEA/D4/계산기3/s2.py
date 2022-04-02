T = "3+(4+5)*6+7"

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

print(stack)