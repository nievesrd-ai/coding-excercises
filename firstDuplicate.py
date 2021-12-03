def firstDuplicate(a):
    answer = -1
    array_length = len(a)
    best_duplicate_index =  array_length - 1

    for j in range(0, array_length):
        current_value = a[j]
        for m in range(j + 1, array_length):
            if m < array_length:
                if current_value == a[m]:
                    if m <= best_duplicate_index:
                        best_duplicate_index = m
                        answer = current_value
    print(answer)
    return(answer)

a = [3, 3, 3]
firstDuplicate(a)