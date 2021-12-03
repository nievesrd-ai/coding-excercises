def ll2list(current_node):
    output = []
    while True:
        output.append(current_node.value)
        if current_node.next:
            current_node = current_node.next
        else:
            break
    return output

def solution(ll1, ll2):
    if ll1 is None:
        return ll2
    if ll2 is None:
        return ll1
    answer = []

    current_node_1 = ll1
    current_node_2 = ll2
    accumulator = []
    end_of_1 = False
    end_of_2 = False
    while True:
        if current_node_1.value < current_node_2.value:
            accumulator.append(current_node_1.value)
            if current_node_1.next:
                current_node_1 = current_node_1.next
            else:
                end_of_1 = True
        else:
            accumulator.append(current_node_2.value)
            if current_node_2.next:
                current_node_2 = current_node_2.next
            else:
                end_of_2 = True
        if end_of_1:
            answer = accumulator + ll2list(current_node_2)
            break
        if end_of_2:
            answer = accumulator + ll2list(current_node_1)
            break
    return answer