# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map = set()
        i = -1      # index
        p = head    # pointer

        while head not in map and head != None:
            map.add(head)
            head = head.next

        if head == None:
            return False

        return True