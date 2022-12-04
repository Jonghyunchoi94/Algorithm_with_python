import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, W = map(int, input().split())

