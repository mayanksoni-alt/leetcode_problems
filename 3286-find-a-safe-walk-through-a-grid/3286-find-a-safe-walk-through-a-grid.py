class Solution(object):
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        pq = []
        start = grid[0][0]
        heappush(pq, (start, 0, 0))

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = start

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            cost, x, y = heappop(pq)

            if x == m - 1 and y == n - 1:
                return cost < health

            if cost > dist[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heappush(pq, (new_cost, nx, ny))

        return False
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        