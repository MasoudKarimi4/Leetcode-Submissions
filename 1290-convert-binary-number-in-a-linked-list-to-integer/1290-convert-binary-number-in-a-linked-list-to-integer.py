# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        
        if head == None:
            return 0 
        
        nums = []
        
        cur = head
        
        while cur != None:
            nums.append(cur.val)
            
            cur = cur.next
            
        print(nums)
            
        nums = nums[::-1]
        
        number= 0
        
        for i in range(len(nums)):
            
            if nums[i] == 1:
                number += (2**i)
            
        return number 
        