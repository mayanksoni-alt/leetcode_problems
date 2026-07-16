class Solution(object):
    def gcdSum(self, nums):

        prefix_max = nums[0]

        for i in range(len(nums)):
            if nums[i] > prefix_max:
                prefix_max = nums[i]

            a = prefix_max
            b = nums[i]

            while b:
                a, b = b, a % b

                nums[i] = a

        nums.sort()

        left = 0
        right = len(nums) - 1
        ans = 0

        while left < right:
            a = nums[left]
            b = nums[right] 
            while b:
                a, b = b, a % b
            ans += a
            left += 1
            right -= 1

        return ans
        