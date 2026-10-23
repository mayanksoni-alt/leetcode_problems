
class Solution(object):
    def sortPermutation(self, nums):
        k = -1

        for i in range(len(nums)):
            if nums[i] != i:
                k &= nums[i]

        return max(k, 0)
