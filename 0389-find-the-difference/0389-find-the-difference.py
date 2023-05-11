class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dict = {}
        
        tdict = {}
        
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        for i in t:
            if i not in tdict:
                tdict[i] = 1
            else:
                tdict[i] += 1
        
       
        for i in t:
            if i not in s:
                return i 
            else:
                if tdict[i] != dict[i]:
                    return i 
                
        