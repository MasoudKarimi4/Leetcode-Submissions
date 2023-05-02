class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num = 1
        
        for i in nums:
            num *= i
            
        print(num)    
        if num > 0:
            return 1
        elif num == 0:
            return 0
        elif num < 1:
            return -1 
        