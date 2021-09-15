n = 3
m = 12


def solution(n, m):
    gcd = -1
    lcm = -1
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    for j in range(1, n * m + 1):
        if j % n == 0 and j % m == 0:
            lcm = j
            break
    answer = [gcd, lcm]

    return answer

print(solution(n, m))