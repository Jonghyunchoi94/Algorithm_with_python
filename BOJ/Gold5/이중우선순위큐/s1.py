import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())

for _ in range(T):
    k = int(input())
    heap = []
    for _ in range(k):
        method, number = input().split()
        if method == 'I':
            heapq.heappush(heap, int(number))
        elif method == 'D':
            if number == '-1':
                if heap:
                    heapq.heappop(heap)
            elif number == '1':
                heapq.heapify(heap)
                if heap:
                    heap.pop()

    if not heap:
        print("EMPTY")
    else:
        print(heap[-1], heap[0])


