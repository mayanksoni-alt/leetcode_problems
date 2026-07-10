class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((v, i) for i, v in enumerate(nums))

        pos = [0] * n
        group = [0] * n

        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        g = 0
        for i in range(1, n):
            if arr[i][0] - arr[i - 1][0] > maxDiff:
                g += 1
            group[i] = g

        LOG = 18
        jump = [[0] * n for _ in range(LOG)]

        j = 0
        for i in range(n):
            while j + 1 < n and arr[j + 1][0] - arr[i][0] <= maxDiff:
                j += 1
            jump[0][i] = j

        for k in range(1, LOG):
            for i in range(n):
                jump[k][i] = jump[k - 1][jump[k - 1][i]]

        ans = []

        for u, v in queries:
            pu = pos[u]
            pv = pos[v]

            if pu > pv:
                pu, pv = pv, pu

            if group[pu] != group[pv]:
                ans.append(-1)
                continue

            if pu == pv:
                ans.append(0)
                continue

            cur = pu
            res = 0

            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < pv:
                    cur = jump[k][cur]
                    res += 1 << k

            ans.append(res + 1)

        return ans
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        