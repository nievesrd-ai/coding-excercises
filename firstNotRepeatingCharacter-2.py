from collections import OrderedDict

def solution(s):
    answer = "_"
    char_index_map = OrderedDict()
    non_repeating_pair = (1E6, "_")
    for index, char in enumerate(s):
        if char_index_map.get(char):
            char_index_map[char].append(index)
        else:
            char_index_map[char] = [index]
    for char in char_index_map.keys():
        if len(char_index_map[char]) == 1:
            answer = char
            break
    return answer

if __name__ == "__main__":
    s = "abacabaabacaba"
    s = "abacabad"

    print(solution(s))