class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict = {}
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        
        for num, oc in dict.items():
            
            if oc == 1:
                return num 
        