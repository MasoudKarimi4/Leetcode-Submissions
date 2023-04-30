class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        lo = 0
        hi = len(nums) - 1 
        
        while lo <= hi:
            
            
            mid = (lo + hi)// 2
            num = nums[mid]
            
            
            if num == target:
                return mid
            elif num < target:
                lo = mid + 1
            elif num > target:
                hi = mid - 1
            
        
        return -1
        