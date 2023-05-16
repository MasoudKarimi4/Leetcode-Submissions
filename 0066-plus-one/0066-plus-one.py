class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        
        num = ""
        
        for i in digits:
            num += str(i)
        
        rnum = int(num)
        
        rnum += 1
        
        list = []
        
        while rnum > 0:
            
            dig = rnum % 10
            
            list.append(dig)
            
            rnum = rnum // 10
            
        return list[::-1]
        