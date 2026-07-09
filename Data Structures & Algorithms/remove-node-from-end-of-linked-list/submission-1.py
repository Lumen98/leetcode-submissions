# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        iterator = head
        while iterator:
            iterator = iterator.next
            length += 1

        iterator = head
        target = length - n
        index = 0
        prev = None

        while iterator:
            if target == 0 and index == 0:                
                return head.next
            if index == target:
                prev.next = iterator.next
                del iterator
                return head
            prev = iterator
            iterator = iterator.next

            index += 1
        
            

