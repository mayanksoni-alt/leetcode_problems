class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i < 0 or j < 0 or board[i][j] == 'X':
                return (-1, 0)

            if board[i][j] == 'E':
                return (0, 1)

            best_score = -1
            ways = 0

            for x, y in ((i - 1, j), (i, j - 1), (i - 1, j - 1)):
                score, cnt = dfs(x, y)

                if score > best_score:
                    best_score = score
                    ways = cnt
                elif score == best_score and score != -1:
                    ways = (ways + cnt) % MOD

            if best_score == -1:
                memo[(i, j)] = (-1, 0)
                return memo[(i, j)]

            val = 0
            if board[i][j].isdigit():
                val = int(board[i][j])

            memo[(i, j)] = (best_score + val, ways)
            return memo[(i, j)]

        score, ways = dfs(n - 1, n - 1)

        if ways == 0:
            return [0, 0]

        return [score, ways]