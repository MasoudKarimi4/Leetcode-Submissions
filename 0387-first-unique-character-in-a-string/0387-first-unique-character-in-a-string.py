class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict = {}
        
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        
        return -1 
        