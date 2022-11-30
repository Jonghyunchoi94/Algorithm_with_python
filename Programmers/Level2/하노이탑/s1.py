n = 2
def solution(n):
    answer = []

    def hanoi(n, from_p, to_p, rest_p):
        if n == 1:
            answer.append([from_p, to_p])
            return

        hanoi(n - 1, from_p, rest_p, to_p)
        answer.append([from_p, to_p])
        hanoi(n - 1, rest_p, to_p, from_p)
        return

    hanoi(n, 1, 3, 2)

    return answer

print(solution(n))