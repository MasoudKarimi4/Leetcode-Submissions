class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
        n = len(heights)
        
        for i in range(n):
            for p in range(n-1):
                
                if heights[p] < heights[p+1]:
                    
                    heights[p], heights[p+1] = heights[p+1], heights[p]
                    names[p], names[p+1] = names[p+1], names[p]
                            
        return names 
        
        
        