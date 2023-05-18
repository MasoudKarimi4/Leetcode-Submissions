# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        if list1 == None and list2 == None:
            return None
        elif list1 == None and list2 is not None:
            return list2
        elif list2 == None and list1 is not None:
            return list1
        
        

        elem = list1
        elem2 = list2
        
        length = 0
        
        list = []
        
        
        while elem:
            list.append(elem.val)
            length += 1
            elem = elem.next
        
        while elem2:
            list.append(elem2.val)
            length += 1
            elem2 = elem2.next
        
        list = sorted(list)
        
        nodes = []
        
        for i in range(length):
            
            if i == 0:
                nodes.append(ListNode(list[i]))
            else:
                nodes.append(ListNode(list[i]))
                nodes[i-1].next = nodes[i]
        
        head = nodes[0]
        
        return head 
            
            
            
        
        
        
        
            
            