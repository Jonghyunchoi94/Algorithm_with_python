import sys
sys.stdin = open('input.txt')

X = int(sys.stdin.readline())

print(bin(X).count('1'))