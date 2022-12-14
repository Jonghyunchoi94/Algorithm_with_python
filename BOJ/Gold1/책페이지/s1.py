import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

res = [0] * 10

for i in range(1, N + 1):
    temp = str(i)
    for j in range(len(temp)):
        res[int(temp[j])] += 1

print(" ".join(map(str, res)))
