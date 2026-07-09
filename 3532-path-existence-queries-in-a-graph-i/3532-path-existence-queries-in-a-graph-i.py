class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):

        group = [0] * n
        current_group = 0


        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                current_group += 1
            group[i] = current_group

        ans = []
        for u, v in queries:
            ans.append(group[u] == group[v])

        return ans
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        