class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        
        s = s.lower()
        
        for i in s:
            if i not in chars:
                s = s.replace(i, "")
        
        return s == s[::-1]
        