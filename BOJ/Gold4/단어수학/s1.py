import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

storage = {}
answer = 0

for _ in range(N):
    num = sys.stdin.readline().rstrip()

    n = len(num)
    for i in range(n - 1, -1, -1):
        if storage.get(num[n - 1 - i]):
            storage[num[n - 1 - i]] += 10 ** i
        else:
            storage[num[n - 1 - i]] = 10 ** i

sort_info = sorted(storage.values(), reverse=True)

start = 9
for i in sort_info:
    answer += (i * start)
    start -= 1

print(answer)
