from typing import List
import heapq


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        heap = []
        for i, j in enumerate(nums):
            heapq.heappush(heap, (-j, i))

        return heapq.heappop(heap)[1]
