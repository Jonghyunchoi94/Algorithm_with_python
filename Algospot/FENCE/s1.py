import sys

sys.stdin = open('input.txt')

"""
문제 접근 방법
1. 완전탐색
2. 완전탐색의 최적화로 분할 정복 알고리즘 설계

분할 정복 알고리즘 설계
1. 가장 큰 직사각형을 왼쪽 부분 문제에서만 잘라낼 수 있다.
2. 가장 큰 직사각형을 오른쪽 부분 문제에서만 잘라낼 수 있다.
3. 가장 큰 직사각형은 왼쪽 부분 문제와 오른쪽 부분 문제에 걸쳐 있다.
"""


def solve(left, right):
    if left == right:
        return fence[left]

    mid = (left + right) // 2
    ret = max(solve(left, mid), solve(mid + 1, right))
    lo = mid
    hi = mid + 1
    height = min(fence[lo], fence[hi])

    ret = max(ret, height * 2)

    while left < lo or hi < right:
        if hi < right and (lo == left or fence[lo - 1] < fence[hi + 1]):
            hi += 1
            height = min(height, fence[hi])

        else:
            lo -= 1
            height = min(height, fence[lo])

        ret = max(ret, height * (hi - lo + 1))
    return ret


C = int(input())

for case in range(C):
    N = int(input())
    fence = list(map(int, input().split()))

    print(solve(0, len(fence) - 1))
