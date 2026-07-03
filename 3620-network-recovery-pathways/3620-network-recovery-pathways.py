from heapq import heappush, heappop
from math import inf
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        def check(mid: int) -> bool:
            dist = [inf] * n
            dist[0] = 0
            pq = [(0, 0)]

            while pq:
                d, u = heappop(pq)

                if d > k:
                    return False

                if u == n - 1:
                    return True

                if dist[u] < d:
                    continue

                for v, w in g[u]:
                    if w < mid:
                        continue

                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))

            return False

        n = len(online)
        g = [[] for _ in range(n)]

        l = inf
        r = 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)

        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1

        return l if check(l) else -1