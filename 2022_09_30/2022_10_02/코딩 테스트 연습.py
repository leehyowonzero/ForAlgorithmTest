def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for i, problem in enumerate(problems):
        if (problem[0] >= max_alp):
            max_alp = problem[0]
        if (problem[1] >= max_cop):
            max_cop = problem[1]

    dp = [[1000 for _ in range(251)] for _ in range(251)]  # [알고력, 코딩력] = 도달시간
    if (max_alp <= alp and max_cop <= cop):
        return 0
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if (i + 1 >= max_alp):
                dp[max_alp][j] = min(dp[max_alp][j], dp[i][j] + 1)
            else:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if (j + 1 >= max_cop):
                dp[i][max_cop] = min(dp[i][max_cop], dp[i][j] + 1)
            else:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if (i >= alp_req and j >= cop_req):
                    x = i + alp_rwd
                    y = j + cop_rwd
                    if (i + alp_rwd >= max_alp):
                        x = max_alp
                    if (j + cop_rwd >= max_cop):
                        y = max_cop
                    dp[x][y] = min(dp[x][y], dp[i][j] + cost)

    answer = dp[max_alp][max_cop]
    return answer
