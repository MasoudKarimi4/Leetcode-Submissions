# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        num = 0
        
        cur = head
        
        while cur is not None:
            num += 1
            cur = cur.next
        
        
        
        if num % 2 == 0:
            index = (num//2)+ 1
        else:
            index = num / 2 
            index += 1 
        
        print(num,index)
        
        cur = head
        
        it = 1
        
        while cur is not None:
            if it == index:
                return cur
            else:
                it += 1
                cur = cur.next
        
        
        