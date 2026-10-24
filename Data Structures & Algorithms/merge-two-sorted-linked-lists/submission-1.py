# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = result_node = ListNode()

        while list1 and list2: 
            if list1.val < list2.val:               # If list1 < list2
                result_node.next = list1            # Links result_node to list1
                list1 = list1.next                  # Moves list1 forward
            else:                                   # If list1 > list2
                result_node.next = list2            # Links result_node to list2
                list2 = list2.next                  # Moves list2 forward
            result_node = result_node.next          # Moves result_node forward   
        result_node.next = list1 or list2           # If list1 or list2 are unequal and nodes remain

        return dummy_node.next                      # Returns head of merged list