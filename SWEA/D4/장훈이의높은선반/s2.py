import sys
sys.stdin = open('input.txt')

def check(a, s):
    global min_val
    # 직원들의 키를 합한 값이 최소보다 큰 경우 종료
    if s >= min_val:
        return
    # 직원들의 키가 선반보다 높은 경우 실행
    elif a >= N:
        if s >= B and s < min_val:
            min_val = s
        return
    # 직원들의 조합을 만드는 부분
    else:
        visited[a] = 1
        check(a + 1, s + visited[a] * H[a])
        visited[a] = 0
        check(a + 1, s + visited[a] * H[a])


T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    min_val = 1000000000
    visited = [0] * N

    check(0, 0)
    print('#{} {}'.format(t, min_val - B))