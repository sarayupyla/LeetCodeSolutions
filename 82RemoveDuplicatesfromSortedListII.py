# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while current:
            if current.next and current.val== current.next.val:   #if current node is a duplicate
                while current.next and current.val==current.next.val:    #to skip all the duplicates
                     current=current.next
                prev.next=current.next     #so that the duplicates are removed
            else:
                prev=prev.next
            current=current.next
        return dummy.next

