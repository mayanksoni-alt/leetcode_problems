class Solution(object):
    def maxProduct(self, n):
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        max_product = 0


        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                product = digits[i] * digits[j]

                if product > max_product:
                    max_product = product


        return max_product
        """
        :type n: int
        :rtype: int
        """
        