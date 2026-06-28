class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
    
        arr.sort()
        arr[0]=1

        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if(diff > 1):
                arr[i] = arr[i] - diff + 1

        max = arr[-1]

        return max

        """
        :type arr: List[int]
        :rtype: int
        """
        