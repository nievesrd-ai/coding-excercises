def areFollowingPatterns(strings, patterns):
    hash = {j: [] for j in patterns}
    answer = True
    for j in range(0, len(strings)):
        hash[patterns[j]].append(strings[j])
        if len(list(set(hash[patterns[j]]))) > 1:
            answer = False
            return False
    return answer



strings = ["cat", "dog", "dog"]
patterns = ["a", "b",  "b"]


strings = ["cat", "dog", "dog"]
patterns = ["a", "b",  "b"]

areFollowingPatterns(strings, patterns)
