class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rane = 0
        
        for i in nums:
            rane += 1
            
        numbers = []
        
        for i in range(max(nums)+2):
            numbers.append(i)
        
        print(numbers,nums)
        
        for i in numbers:
            if i not in nums:
                return i 
            
        
        
        