class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        list = ""
        index = 0
        while len(word1) > 0 or len(word2) > 0:
            
            if len(word1) > 0:
                
                list += (word1[index])
                
                word1 = word1.replace(word1[index],"",1)
            
            if len(word2) > 0:
                list += (word2[index])
                
                word2 = word2.replace(word2[index],"",1)
        
        print(len(word1),len(word2))

        
        return list
        
        