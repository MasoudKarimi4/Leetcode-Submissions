class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        
        string1 = ''
        string2 = ''
        for e in word1:
            string1 += e
        for g in word2:
            string2 += g
            
        if string1 != string2:
            return False
        else: 
            return True
        