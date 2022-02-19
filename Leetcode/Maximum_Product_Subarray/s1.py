class Solution:
    def maxProduct(self, nums):
        max_num, min_num, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            max_case = max(nums[i], max_num * nums[i], min_num * nums[i])
            min_case = min(nums[i], max_num * nums[i], min_num * nums[i])
            max_num, min_num = max_case, min_case

            res = max(max_num, res)
        return res

a = Solution()
print(a.maxProduct([2,-5,-2,-4,3]))
