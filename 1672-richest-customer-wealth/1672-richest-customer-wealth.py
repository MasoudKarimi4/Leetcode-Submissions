class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        list = []
        
        
        for i in accounts:
            list.append(sum(i))
        
        return max(list)
        