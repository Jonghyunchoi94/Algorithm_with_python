import sys
sys.stdin = open('input.txt')

"""
7662번 pypy만 통과됨!!
"""
import heapq

T = int(input())

for _ in range(T):
    k = int(input())
    max_heap, min_heap = [], []
    visited = [False] * (k + 1)
    for i in range(k):
        method, number = input().split()
        if method == 'I':
            heapq.heappush(min_heap, (int(number), i))
            heapq.heappush(max_heap, (-int(number), i))
            visited[i] = True
        elif method == 'D':
            if number == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif number == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')


