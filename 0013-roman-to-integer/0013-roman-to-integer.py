class Solution(object):
    def romanToInt(self, s):
        
        
        for i in s:
            if 'IV' in s:
                s = s.replace('IV','IIII')
            elif 'IX' in s:
                s = s.replace('IX', 'VIIII')
            elif 'CD' in s:
                s = s.replace('CD', 'CCCC')
            elif 'CM' in s:
                s = s.replace("CM", "DCCCC")
            elif 'XL' in s:
                s = s.replace("XL", "XXXX")
            elif "XC" in s:
                s = s.replace("XC","LXXXX")
            
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
        