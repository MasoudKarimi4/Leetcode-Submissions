class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        for i in s:
            
            if i in ['(', '{', '[']:
                stack.append(i)
            
            else:
                if not stack:
                    return False
                
                curr = stack.pop()
                
                if curr == '[' and i != ']':
                    return False
                if curr == '(' and i != ')':
                    return False
                if curr == '{' and i != '}':
                    return False
        
        if stack:
            return False
            
        return True 
            
        