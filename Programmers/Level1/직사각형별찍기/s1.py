import sys
sys.stdin = open('input.txt')

n, m = map(int, input().strip().split(' '))
print((('*'* n) + '\n')*m)