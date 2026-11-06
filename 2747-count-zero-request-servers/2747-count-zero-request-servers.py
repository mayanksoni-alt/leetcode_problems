class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        count = [0] * (n + 1)
        ans = [0] * len(queries)

        left = 0
        right = 0
        active = 0

        for q, idx in sorted_queries:
            start = q - x

            # Add requests within the right boundary
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            # Remove requests outside the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans