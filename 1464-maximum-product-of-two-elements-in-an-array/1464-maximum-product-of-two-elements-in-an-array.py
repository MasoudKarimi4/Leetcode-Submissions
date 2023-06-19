class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = sorted(nums)
        nums = nums[::-1]
        
        v1, v2 = nums[0], nums[1]
        
        v1 = v1 - 1
        v2 = v2 - 1
        
        
        return v1*v2
        