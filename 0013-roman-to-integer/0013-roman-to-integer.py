class Solution(object):
    def romanToInt(self, s):
        
        
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL','XXXX').replace('XC', 'LXXXX').replace('CD','CCCC').replace('CM','DCCCC')

            
        
        num = 0 
        
        for i in range(len(s)):
            if s[i] == 'I':
                num += 1
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'X':
                num += 10
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'C':
                num += 100
            elif s[i] == 'D':
                num += 500
            elif s[i] == 'M':
                num += 1000
        

            
        return num 
        