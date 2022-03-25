def solution(nums):
    N = len(nums)
    s = set(nums)
    answer = min(len(s), N//2)
    return answer