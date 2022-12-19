import sys
sys.stdin = open('input.txt')

X = int(sys.stdin.readline())

bar = 0
l = 64
res = 0
while bar < X:
    if bar + l <= X:
        bar += l
        res += 1
        if bar == X:
            break

    l //= 2

print(res)