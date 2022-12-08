import sys
sys.stdin = open('input.txt')
from collections import deque
# (100+1+ | 01)+

T = int(sys.stdin.readline())

for _ in range(T):
    strings = sys.stdin.readline().rstrip()

    q = deque(strings)
    s = ""
    Flag = False
    change = 0
    while q:
        now = q.popleft()
        s += now

        if Flag:
            if change == 0 and now == "1":
                change += 1
                if not q:
                    Flag = False
                    change = 0
                    s = ""
            elif change == 1 and now == "0":
                change = 0
                Flag = False
                s = "0"
        else:
            if s == "01":
                s = ""
            elif s == "100":
                Flag = True


    if not s:
        print("YES")
    else:
        print("NO")



