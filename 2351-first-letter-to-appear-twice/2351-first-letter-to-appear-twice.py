class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        dict = {}
        
        
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                return i
        