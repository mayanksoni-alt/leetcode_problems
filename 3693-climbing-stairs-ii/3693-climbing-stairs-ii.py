
class Solution(object):
    def climbStairs(self, n, costs):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for j in range(1, n + 1):
            for jump in range(1, 4):
                i = j - jump

                if i >= 0:
                    cost = costs[j - 1] + (j - i) ** 2
                    dp[j] = min(dp[j], dp[i] + cost)

        return dp[n]
