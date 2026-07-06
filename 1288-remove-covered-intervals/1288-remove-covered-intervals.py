class Solution(object):
    def removeCoveredIntervals(self, intervals):
        count = 0

        for i in range(len(intervals)):
            covered = False

            for j in range(len(intervals)):
                if j == i:
                    continue
            

                if(intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]):
                    covered = True
                    break
            
            if not covered:
                count+=1
        
        return count
    
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        