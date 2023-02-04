class Solution(object):
    def twoSum(self, nums, target):

        answerList = []
        tested = False 

        for i in range(len(nums)):
            for g in range(len(nums)):
                if nums[i] + nums[g] == target and i != g and tested == False:
                    answerList.append(i)
                    answerList.append(g)
                    tested = True
                    break
    

        return answerList 