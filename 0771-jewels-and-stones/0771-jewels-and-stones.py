class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        num = 0
        
        for i in stones:
            if i in jewels:
                num += 1
        
        return num 