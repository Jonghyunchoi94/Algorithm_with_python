import re
import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    string = sys.stdin.readline().replace('\n', '')
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(string)
    if m:
        print("YES")
    else:
        print("NO")
