class Solution(object):
    def twoSum(self, nums, target):

        table = {}
        sums = []
        
        for i in range(len(nums)):
            

            number = target - nums[i]
            print(number)

            if number in table:
                return (table[number],i)
            else:
                table[nums[i]] = i
        