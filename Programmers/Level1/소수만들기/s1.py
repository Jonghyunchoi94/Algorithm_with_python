nums = [1,2,3,4]

from itertools import combinations

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


def listSum(nums, idx):
    res = 0
    for i in idx:
        res += nums[i]
    return res


def solution(nums):
    answer = 0

    comb = list(combinations(range(len(nums)), 3))
    # print(comb)
    for i in comb:
        if isPrime(listSum(nums, i)):
            answer += 1

    return answer

print(solution(nums))