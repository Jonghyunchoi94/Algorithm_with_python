import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
temp = [''] * 50
for _ in range(N):
    d = sys.stdin.readline().rstrip()

    for i in range(len(d)):
        if not temp[i]:
            temp[i] = d[i]
        elif temp[i] != d[i]:
            temp[i] = '?'

res = ''.join(temp).rstrip()
print(res)