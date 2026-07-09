"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # old node--> (new node, random node)
        hashmap = {}


        iterator = head
        while iterator:
            newNode = Node(iterator.val)

            hashmap[iterator] = newNode

            iterator = iterator.next


        iterator = head
        prev = None
        newHead = None
        while iterator:
            if iterator.random in hashmap.keys():
                random = hashmap[iterator.random]
                hashmap[iterator].random = random
            else:
                hashmap[iterator].random = None
            if prev:
                hashmap[prev].next = hashmap[iterator]
            else:
                newHead = hashmap[iterator]
            prev = iterator
                
            iterator = iterator.next


        return newHead











