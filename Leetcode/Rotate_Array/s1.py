"""
list vs list[:]
list[:] 는 shallow copy 즉, 얕은 복사를 의미한다.
"""

class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]