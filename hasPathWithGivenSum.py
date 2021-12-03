#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

        

def enter_and_check(current_node, to_check, cum_sum, answer):
    if answer is False:
        cum_sum = cum_sum + current_node.value
        leaf_node = (current_node.left is None) and (current_node.right is None)
 
        if cum_sum == to_check and leaf_node:
            answer = True
            return answer
        else:
            if current_node.left is not None:
                temp_answer = enter_and_check(current_node.left, to_check, cum_sum, answer)
                answer = answer or temp_answer

            if current_node.right is not None:
                temp_answer = enter_and_check(current_node.right, to_check, cum_sum, answer)
                answer = answer or temp_answer

        return answer
    else:
        return answer

def hasPathWithGivenSum(t, s):
    # perform a depth first search
    # each next steps carries the cummulative sum of values on branch
    cum_sum = 0
    current_node = t # 4
    answer = False
    if t is not None:
        answer = enter_and_check(current_node, s, cum_sum, answer)
    return answer 
