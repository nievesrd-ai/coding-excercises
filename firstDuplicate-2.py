def solution(arr):
    answer = -1
    num2indxmap = {}
    for indx, value in enumerate(arr):
        if num2indxmap.get(value):
            num2indxmap[value].append(indx)
            answer = value
            break
        else:
            num2indxmap[value] = [indx]
    return answer

if __name__ == "__main__":
    arr = [2, 1, 3, 5, 3, 2]
    arr = [2, 4, 3, 5, 1]
    arr = [2, 2]
    print(solution(arr))