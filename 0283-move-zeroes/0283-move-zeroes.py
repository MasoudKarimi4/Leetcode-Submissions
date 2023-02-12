class Solution(object):
    def moveZeroes(self, nums):
        
        new = []

        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                new.append(nums[i])

        for i in range(zeros):
            new.append(0)

        nums[:] = new 
        
        
        
                
                
        