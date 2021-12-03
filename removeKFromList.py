class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.special_case = False
        if head is None:
            print("Catched")
            self.head = ListNode(None)
            self.special_case = True
        else:
            self.head = head
        
    def append_values(self, values):
        current_node = self.head
        #getting to end of linked list
        was_empty = False
        if current_node is None:
            was_empty = True
            self.head = ListNode(values[0])
            current_node= self.head
        while current_node.next:
            current_node = current_node.next
        if was_empty:
            start_index = 1
        else:
            start_index = 0
        for j in range(start_index, len(values)):
            value = values[j]
            new_node = ListNode(value)
            current_node.next = new_node
            current_node = current_node.next

    def find_and_delete_value(self, k):

        while self.head:
            if self.head.value == k:
                # Guarantees head will contain one of the values to be deleted
                self.head = self.head.next
            else:
                break
        if self.head: # We might end up witout head
            current_node = self.head.next
            previous_node = self.head
            if current_node:
                keep_going = True
            else:
                keep_going = False
            
            # Only handles cases on which the linked list has at least 2 elements
            # cases with 1 or 0 nodes should be be handled on solution as special cases
            # if current_node.next is not None:
            while keep_going:

                if current_node.value == k:
                    previous_node.next = current_node.next
                previous_node = current_node
                current_node = current_node.next
                if current_node.next is None:
                    if current_node.value == k:
                        previous_node.next = None
                    keep_going = False
                    
        return

    def linked_to_list(self):
        output = []
        current_node = self.head
        while current_node:
            output.append(current_node.value)
            current_node = current_node.next
        return output
            



def solution(l, k):
    linked_list = LinkedList(l)
    if linked_list.head.next is not None:
        linked_list.find_and_delete_value(k)
        return linked_list.linked_to_list()
    else:
        if linked_list.head.value == k:
            return []
        else:
            if linked_list.special_case == False:
                return [linked_list.head.value]
            else:
                return []