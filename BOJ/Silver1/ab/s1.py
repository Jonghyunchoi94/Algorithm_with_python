import sys
sys.stdin = open('input.txt')

from collections import deque

A, B = map(int, input().split())

res = -1
q = deque([(A, 1)])

while q:
    now, cnt = q.popleft()
    if now == B:
        # 만들 수 없는 경우 고려
        res = cnt
        break

    # 메모리 사용량 최적화
    if now * 2 <= B:
        q.append((now * 2, cnt + 1))
    if int(str(now) + '1') <= B:
        q.append(((int(str(now) + '1')), cnt + 1))

print(res)
