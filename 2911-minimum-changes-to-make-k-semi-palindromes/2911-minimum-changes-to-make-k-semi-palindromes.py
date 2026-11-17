
class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)

        cost = [[float('inf')] * n for _ in range(n)]

        # Precompute minimum changes for every substring
        for d in range(1, n):
            same = [[0] * n for _ in range(n)]

            for m in range(2, n // d + 1):
                for i in range(n - m * d + 1):
                    j = i + m * d - 1

                    changes = 0

                    # Compare outer characters of each group
                    for r in range(d):
                        if s[i + r] != s[j - d + 1 + r]:
                            changes += 1

                    if m > 2:
                        changes += same[i + d][j - d]

                    same[i][j] = changes
                    cost[i][j] = min(cost[i][j], changes)

        # DP: divide string into exactly k parts
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                for prev in range(2 * (parts - 1), i - 1):
                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[prev][parts - 1] + cost[prev][i - 1]
                    )

        return dp[n][k]
