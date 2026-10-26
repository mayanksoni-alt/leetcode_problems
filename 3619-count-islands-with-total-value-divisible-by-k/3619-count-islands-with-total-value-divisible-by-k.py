class Solution:
    def countIslands(self, grid, k):
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0

            value = grid[r][c]
            grid[r][c] = 0  # Mark visited

            value += dfs(r + 1, c)
            value += dfs(r - 1, c)
            value += dfs(r, c + 1)
            value += dfs(r, c - 1)

            return value

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    total = dfs(r, c)

                    if total % k == 0:
                        count += 1

        return count