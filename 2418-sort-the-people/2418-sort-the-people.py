class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
        dList = []
        
        for i in range(len(heights)):
            
            temp = [heights[i], [names[i]]]
            dList.append(temp)
            
        sort = sorted(dList)
        sort = sort[::-1]
        
        nameList = []
        
        for i in range(len(names)):
            nameList.append(sort[i][1][0])
        
        return nameList 
        
        