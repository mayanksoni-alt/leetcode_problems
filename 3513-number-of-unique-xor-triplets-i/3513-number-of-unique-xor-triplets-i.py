class Solution(object):
    def uniqueXorTriplets(self, nums):
    
        n = len(nums)

        if n == 1:
            return 1
        if n == 2:
            return 2

        ans = 1
        while ans <= n:
            ans <<= 1

        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        