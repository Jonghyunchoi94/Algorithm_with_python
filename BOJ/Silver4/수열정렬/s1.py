import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

P = []
B = sorted(A)

for i in range(N):
    P.append(B.index(A[i]))
    B[B.index(A[i])] = -1


# unpacking   (*) => 컨테이너 타입의 데이터 unpacking
print(*P)

# print(' '.join(map(str, P)))

