class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        if n % 2 != 0 and n != 1 or n == 0 or n < 0:
            return False 
        
        while n > 0:
            
            n = n // 2
            
            if n % 2 != 0 and n != 1:
                return False
            
        return True 
        