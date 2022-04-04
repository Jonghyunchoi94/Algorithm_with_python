import sys
sys.stdin = open('input2.txt')

def solve(items, K):
    N = len(items)
    lengths = [len(str(i)) for i in items]
    total_len = sum(lengths)
    mods = []
    # mod[i][d]: items[i]*10**d % K
    for i in items:
        mods.append([i % K])
        for d in range(1, total_len + 1):
            mods[-1].append((mods[-1][-1] * 10) % K)

    dp = [[-1 for _ in range(K)] for _ in range(1 << N)]
    # dp[state][k]: the number of perms, each of which consists of items denoted by state and = k (mod K)

    for d in range(N):
        dp[1 << d] = [1 if k == mods[d][0] else 0 for k in range(K)]

    def dfs(state, residue, cur_len):
        if dp[state][residue] >= 0:
            return dp[state][residue]
        val = 0
        for d in range(N):
            if (1 << d) & state:
                remaining_len = cur_len - lengths[d]
                state_ = state ^ (1 << d)
                residue_ = (residue - mods[d][remaining_len]) % K
                val += dfs(state_, residue_, remaining_len)
        dp[state][residue] = val
        return val

    ans = dfs((1 << N) - 1, 0, total_len)
    return ans


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    k = int(input())
    ans = solve(nums, k)
    print(f"#{test_case} {ans}")