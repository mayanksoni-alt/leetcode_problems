import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][run] = minimum cost to reach
        # node with a consecutive character count of run
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, u, run = heapq.heappop(pq)

            if cost != dist[u][run]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    new_run = run + 1
                else:
                    new_run = 1

                if new_run > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_run]:
                    dist[v][new_run] = new_cost
                    heapq.heappush(
                        pq, (new_cost, v, new_run)
                    )

        return -1