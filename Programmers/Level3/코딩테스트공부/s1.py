alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]

def solution(alp, cop, problems):
    alp_tgt = max([alp_req for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems])
    cop_tgt = max([cop_req for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems])
    if alp >= alp_tgt and cop >= cop_tgt:
        return 0

    alp_tgt = max(alp_tgt, alp)
    cop_tgt = max(cop_tgt, cop)

    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    dp = [[float('inf') for c in range(cop_tgt + 1)] for r in range(alp_tgt + 1)]
    dp[alp][cop] = 0
    for r in range(alp, alp_tgt + 1):
        for c in range(cop, cop_tgt + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if r < alp_req or c < cop_req:
                    continue
                nr, nc = min(r + alp_rwd, alp_tgt), min(c + cop_rwd, cop_tgt)
                dp[nr][nc] = min(dp[nr][nc], dp[r][c] + cost)

    return dp[-1][-1]

print(solution(alp, cop, problems))
