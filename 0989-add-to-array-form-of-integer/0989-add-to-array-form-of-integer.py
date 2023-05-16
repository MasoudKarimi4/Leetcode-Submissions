class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        stri = ""
        
        for i in num:
            stri += str(i)
        
        arnum = int(stri)
        
        numero = arnum + k
        
        list = []
        
        while numero > 0:
            
            dig = numero % 10
            
            list.append(dig)
            
            numero = numero //  10
        
        return(list[::-1])
        