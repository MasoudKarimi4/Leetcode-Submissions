class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        rev = []
        
        if ch not in word:
            return word
        
        for i in word:
            if i == ch:
                rev.append(i)
                break
            else:
                rev.append(i)
        
        substring = ""
        
        for i in rev:
            substring += i
            
        
        revString = substring[::-1]
                  
        
        word = word.replace(substring,revString)

        
        return word 
        
        
        