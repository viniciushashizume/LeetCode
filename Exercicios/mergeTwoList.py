# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1734967712/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newList = []
        current = list1
        while current:
            newList.append(current.val)
            current = current.next
        
        current = list2
        while current:
            newList.append(current.val)
            current = current.next
            
        newList.sort()
        
        if not newList:
            return None

        head = ListNode(0) 
        current_new = head

        for valor in newList:
            novo_no = ListNode(valor)
            current_new.next = novo_no
            current_new = current_new.next

        return head.next