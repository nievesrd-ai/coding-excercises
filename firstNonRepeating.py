def firstNotRepeatingCharacter(s):
    answer = "_"
    to_check = [True] * len(s)
    for j in range(0, len(s)):
        current_character = s[j]
        match_found = False
        if j + 1 < len(s):            
                for p in range(j + 1, len(s)):
                    if to_check[p]:
                        future_character = s[p]
                        if current_character == future_character:
                            to_check[p] = False
                            match_found = True
                            break
                if match_found == False:
                    answer = current_character
                    break
    return answer

in_str = "abacabad"                
# in_str = "abacabaabacaba"
print(firstNotRepeatingCharacter(in_str))