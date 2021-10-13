import sys
sys.stdin = open('input.txt')

from copy import deepcopy

T = int(input())

for case in range(T):
    N, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
