class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
    
        dict = {}
        
        types = 0
        n = 0
        
        for i in candyType:
            if i not in dict:
                dict[i] = 1
                types += 1
            
            n += 1
        
        eat = n / 2
        
        if eat > types:
            return types
        else:
            return eat 
                
                
                