class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        num = 0
        
        for i in grid:
            for g in i:
                if g < 0:
                    num += 1
        
        return num 
        
        
        
        
        
        
        
        