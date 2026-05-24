# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next: 
            fast=fast.next.next
            slow=slow.next
            if slow==fast: #when both meet we say there is cycle and have to find starting node of the cycle
                temp=head
                while temp!=slow: 
                    temp=temp.next #we more temp and slow one step at a time and when both meet we get starting point
                    slow=slow.next
                return temp
        return None
