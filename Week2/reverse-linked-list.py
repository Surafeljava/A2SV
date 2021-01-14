# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head==None):
            return head
        a,b = self.reverse(head)
        return b
    
    def reverse(self, head: ListNode) -> (ListNode, ListNode):
        if(head.next == None):
            return (head, head)
        
        rev, result = self.reverse(head.next)
        head.next = None
        rev.next = head
        return (head, result)
