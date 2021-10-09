import sys
sys.stdin = open('input.txt')

def tower(height):
    global ans
    if height >= ans:
        return

    if height >= B:
        if ans > height:
            ans = height
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                tower(height + H[i])
                visited[i] = 0


T = int(input())

for case in range(T):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    visited = [0] * N
    ans = 987654321
    tower(0)
    print('#{} {}'.format(case + 1, ans - B))

