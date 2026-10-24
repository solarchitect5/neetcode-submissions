# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head_node: Optional[ListNode]) -> Optional[ListNode]:
        
        current_node    = head_node
        previous_node   = None

        while current_node:
            temp_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = temp_node

        return previous_node