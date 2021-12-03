# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def add_node(self, in_node):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = in_node
        
    def sort_insert(self, start_node, in_node):
        current_node = start_node
        found_location = False
        while current_node:
            if (current_node.val >= in_node.val):
                found_location = True
                break
            previous_node = current_node
            current_node = current_node.next

        if found_location:
            prev_next = current_node.next
            prev_value = current_node.val
            current_node.val = in_node.val
            current_node.next = in_node.next
            if current_node.next:
                self.sort_insert(current_node.next, ListNode(prev_value, prev_next))
            else:
                current_node.next = ListNode(prev_value, prev_next)
                return
        return
            
            
        

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linked = LinkedList(l1)
        linked.sort_insert(linked.head, l2)
        return linked.head