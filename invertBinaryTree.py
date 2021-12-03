# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # do a breadth first traversal
        # on each level, do right becomes left, left becomes right, before queueing the nodes
        import collections
        node_queue = collections.deque()
        level = 0
        if root:
            node_queue.append(root)
        else:
            return root
        
        while node_queue:
            nodes_in_level = len(node_queue)
            while nodes_in_level:
                current_node = node_queue.popleft()
                new_right_node = current_node.left
                new_left_node = current_node.right
                
                current_node.left = new_left_node
                current_node.right = new_right_node
                
                if current_node.left:
                    node_queue.append(current_node.left) 
                if current_node.right:
                    node_queue.append(current_node.right)        
                nodes_in_level-=1
            level+=1
        
        return root