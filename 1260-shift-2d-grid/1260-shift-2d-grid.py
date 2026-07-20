class Solution(object):
    def shiftGrid(self, grid, k):
    
        m = len(grid)
        n = len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        total = m * n
        k %= total
        arr = arr[-k:] + arr[:-k]

        ans = []
        for i in range(0, total, n):
            ans.append(arr[i:i+n])

        return ans

        
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        