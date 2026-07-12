class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {}

        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]

        return arr

        """
        :type arr: List[int]
        :rtype: List[int]
        """
        