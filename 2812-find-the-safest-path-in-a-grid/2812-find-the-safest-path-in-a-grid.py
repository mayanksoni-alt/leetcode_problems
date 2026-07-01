class Solution(object):
    def maximumSafenessFactor(self, grid):

        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Multi-source BFS
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        def canReach(limit):
            if dist[0][0] < limit:
                return False

            visited = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visited[0][0] = True

            while q:
                x, y = q.popleft()

                if x == n - 1 and y == n - 1:
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < n
                        and 0 <= ny < n
                        and not visited[nx][ny]
                        and dist[nx][ny] >= limit
                    ):
                        visited[nx][ny] = True
                        q.append((nx, ny))

            return False

        low = 0
        high = max(max(row) for row in dist)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if canReach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        