class Solution(object):
    def sequentialDigits(self, low, high):
        digits = "123456789"
        ans = []

        for length in range(2, 10):          # number of digits
            for start in range(10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        