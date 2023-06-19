class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        alts = []
        
        alts.append(0)
        sums = 0
        
        for i in gain:
            
            sums += i
            alts.append(sums)
            
        
        
        return max(alts)
        