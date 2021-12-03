#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
import collections

def traverse(node_deque):
    level = 0
    values_at_level = {}
    while node_deque:
        nodes_at_level = len(node_deque)
        while nodes_at_level:
            current_node = node_deque.popleft()
            if str(level) not in values_at_level.keys():
                values_at_level[str(level)] = []
            values_at_level[str(level)].append(current_node.value)
            if current_node.left:
                node_deque.append(current_node.left)
            if current_node.right:
                node_deque.append(current_node.right)
            nodes_at_level-=1
        level+=1
    return values_at_level
    

def largestValuesInTreeRows(t):
    # Depth first search
    # Keep track of levels
    # Store values on each level on a hash table, where key is level, value is list of values at level
    answer = []
    if t:
        node_deque = collections.deque()
        node_deque.append(t)
    else:
        return answer
        
    values_at_level = traverse(node_deque)
    for level in values_at_level.keys():
        answer.append(max(values_at_level[level]))
    return answer