# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
import collections
def traverse(node_queue, node_counter, answer):
    # check if we still have nodes to traverse
    while node_queue and answer:
        current_node = node_queue.pop()
        if current_node.left:
            node_queue.appendleft(current_node.left)
            node_counter['left']+=1
            left_node = current_node.left
        if current_node.right:
            node_queue.appendleft(current_node.right)
            node_counter['right']+=1
            right_node = current_node.right
        answer = check_symmetry(left_node, right_node)

    return  node_counter , answer                                                                   

def check_symmetry(left_node, right_node):
    if left_node and right_node:
        answer = (left_node.right.value == right_node.left.value) and \
            (left_node.left.value == right_node.right)
    else:
        answer = left_node == right_node
    return answer



# left: [2, 3, 4, 5, 7, 8, 6]
# right: [2, 4, 3, 6, 8, 7, 5] 
   
    
def isTreeSymmetric(t):
    # Option one is to traverse all nodes and leafs keeping track
    # of all left and right nodes. If at the end of the scan,
    # there is a mismatch on left an right number of nodes, the answer
    # is false. However, there may be ways to exit earlier if at a given
    # level, if there is no matching left for a right, or right for a left
    # lets breadth first traversal
    answer = True
    node_queue = collections.deque()
    if t:
        node_queue.append(t)
        node_counter = {"left": 0, "right": 0}
        node_counter = traverse(node_queue, node_counter, answer)
    else:
        answer = True
    return answer
