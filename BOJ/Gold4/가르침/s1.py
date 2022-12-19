import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())


storage = set()

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    for i in word:
        storage.add(i)

storage = list(storage)

print(storage)