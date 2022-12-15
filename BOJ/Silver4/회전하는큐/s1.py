import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

pos = list(map(int, sys.stdin.readline().split()))

q = [i for i in range(1, N + 1)]
q = deque(q)

res = 0
s = 0
n = len(pos)

while n > s:
    idx = q.index(pos[s])
    if q[0] == pos[s]:
        q.popleft()
        s += 1
    elif idx > (len(q) // 2):
        for _ in range(len(q) - idx):
            res += 1
            q.appendleft(q.pop())
    else:
        for _ in range(idx):
            res += 1
            q.append(q.popleft())


print(res)