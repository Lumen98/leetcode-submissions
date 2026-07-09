# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        root = dummy

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    newNode = ListNode(list1.val)
                    dummy.next = newNode
                    list1 = list1.next
                else:
                    newNode = ListNode(list2.val)
                    dummy.next = newNode
                    list2 = list2.next
            elif list1:
                newNode = ListNode(list1.val)
                dummy.next = newNode
                list1 = list1.next
            elif list2:
                newNode = ListNode(list2.val)
                dummy.next = newNode
                list2 = list2.next
            dummy = dummy.next


        return root.next




                
