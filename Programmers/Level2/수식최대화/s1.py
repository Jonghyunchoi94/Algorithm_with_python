expression = "100-200*300-500+20"

import re
from itertools import permutations

def solution(expression):
    answer = 0
    exp_per = list(permutations(['-', '+', '*'], 3))

    for i in exp_per:
        idx = 0
        exp_str = re.split('([-,+,*])', expression)
        while idx < 3:
            stack = [exp_str[0]]
            for j in range(1, len(exp_str)):
                stack.append(exp_str[j])
                if exp_str[j - 1] == i[idx]:
                    num2 = stack.pop()
                    operator = stack.pop()
                    num1 = stack.pop()
                    if operator == '+':
                        stack.append(int(num1) + int(num2))
                    elif operator == '-':
                        stack.append(int(num1) - int(num2))
                    elif operator == '*':
                        stack.append(int(num1) * int(num2))
            exp_str = stack
            idx += 1
        answer = max(answer, abs(stack[0]))

    return answer


print(solution(expression))