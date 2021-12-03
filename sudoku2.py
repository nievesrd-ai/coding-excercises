import collections
def check_vector(vec_dict):
    good_vec = True
    del vec_dict['.']
    if vec_dict:
        for vec in vec_dict.keys():
            if vec_dict[vec] > 1:
                good_vec = False
    
    return good_vec
            

def sudoku2(grid):
    answer = True
    for row in range(0,9):
        vals_in_row = collections.Counter(grid[row])
        answer = check_vector(vals_in_row)
        if answer is False:
            return answer
    
    for col in range(0,9):
        current_col = []
        for row in range(0,9):
            current_col.append(grid[row][col])
        vals_in_col = collections.Counter(current_col)
        answer = check_vector(vals_in_col)
        if answer is False:
            return answer
    start_rows = [0, 3, 6]
    end_rows = [3, 6, 9]

    start_cols = [0, 3, 6]
    end_cols = [3, 6, 9]
    
    j = 0
    subgrid = []
    for j in range(0, 3):
        subgrid_counter = collections.Counter()
        start_row = start_rows[j]
        end_row = end_rows[j]
        for k in range(0, 3):
            start_col = start_cols[k]
            end_col = end_cols[k]
            subgrid = []
            subgrid_counter = collections.Counter()
            for row in range(start_row, end_row):
                subgrid.append(grid[row][start_col:end_col])
                subgrid_counter.update(grid[row][start_col:end_col])
            answer = check_vector(subgrid_counter)
            if answer is None:
                hold_it = 1
            if answer is False:
                return answer
    return answer

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],\
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],\
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],\
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],\
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],\
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],\
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],\
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],\
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
answer = sudoku2(grid)
print(answer)