class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        a = nums[0]
        b = nums[len(nums)-1]

        while b:
            a , b = b, a % b

        return a
        """
        :type nums: List[int]
        :rtype: int
        """
        