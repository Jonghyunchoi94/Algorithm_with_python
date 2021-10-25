import sys
sys.stdin = open('input.txt')

from collections import defaultdict

def pre_order(start):
    if start != '.':
        print(start, end='')
        pre_order(tree[start][0])
        pre_order(tree[start][1])

def in_order(start):
    if start != '.':
        in_order(tree[start][0])
        print(start, end='')
        in_order(tree[start][1])

def post_order(start):
    if start != '.':
        post_order(tree[start][0])
        post_order(tree[start][1])
        print(start, end='')


N = int(input())

tree = defaultdict(list)
for case in range(N):
    parent, left, right = input().split()
    tree[parent].append(left)
    tree[parent].append(right)

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()

