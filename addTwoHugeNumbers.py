# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
import collections

class Node(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insert_list(self, in_list_deque):
        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
        else:
            if in_list_deque:
                self.head = Node(in_list_deque.popleft())
                current_node = self.head
            else:
                return
        
        while in_list_deque:
            current_node.next = Node(in_list_deque.popleft())
            current_node = current_node.next  

        return
        
def number_forming(node_list):
    current_full_number = ''        
    keep_going = True
    if node_list:
        current_node = node_list.head
    while current_node:
        current_full_number = current_full_number + "{:04n}".format(current_node.value)
        current_node = current_node.next
    return int(current_full_number)

def list_forming(number):
    strnum = str(number)
    start = len(strnum) - 4
    end = len(strnum)
    out_list = []
    while True:
        out_list.append(int(strnum[start:end]))
        if start == 0:
            out_list.reverse()
            break
        end = start
        start = start - 4
        if start < 0:
            start = 0
    return out_list
def linked_list_gen(in_list):

    in_list =  collections.deque(in_list)
    linked_list = LinkedList()
    linked_list.insert_list(in_list)

    return linked_list
        
                
def addTwoHugeNumbers(a, b):
    num_a = number_forming(a)
    num_b = number_forming(b)
    num_sum = num_a + num_b
    num_sum_list = list_forming(num_sum)
    answer = linked_list_gen(num_sum_list)
    return answer

a = [9876, 5432, 1999]
b = [100, 100, 100]

a_ll = linked_list_gen(a)
b_ll = linked_list_gen(b)
answer = addTwoHugeNumbers(a_ll, b_ll)
