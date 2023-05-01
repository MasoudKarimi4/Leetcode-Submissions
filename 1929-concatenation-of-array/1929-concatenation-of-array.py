class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        list = nums
        
        for i in range(len(nums)):
            list.append(nums[i])
        
        return list 