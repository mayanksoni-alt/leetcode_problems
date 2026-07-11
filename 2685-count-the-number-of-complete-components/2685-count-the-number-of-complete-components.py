class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            component.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i)

                k = len(component)
                complete = True

                for node in component:
                    if len(graph[node]) != k - 1:
                        complete = False
                        break

                if complete:
                    ans += 1

        return ans
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        