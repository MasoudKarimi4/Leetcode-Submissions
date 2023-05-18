# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        sums = []
        list = []
        
        elem = head
        
        while elem:
            list.append(elem.val)
            elem = elem.next
        
        for i in range(len(list)):
            
            num = list[i] + list[len(list)-1-i]
            
            sums.append(num)
        
        return max(sums)
            
            
            
            
        