class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        sum = 0 
        count = 0 
        
        for i in salary:
            if i != max(salary) and i != min(salary):
                count += 1
                sum += i
        
        num = float(float(sum) / float(count))
        
        return num
    