class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sumOdd =1
        sumEven = 2
        odd = 1
        even =2

        for i in range(1 , n):
            odd += 2
            sumOdd += odd 
            even += 2
            sumEven += even

        while sumEven:
            sumOdd, sumEven = sumEven, sumOdd % sumEven
        return sumOdd

        """
        :type n: int
        :rtype: int
        """
        