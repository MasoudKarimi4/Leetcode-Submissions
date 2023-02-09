class Solution(object):
    def isPalindrome(self, x):
        

        reverse = str(x)[::-1]
        print(reverse)
        
        if reverse == str(x):
            return True
        else:
            return False
        
        