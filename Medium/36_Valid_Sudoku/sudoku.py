# 36. Valid Sudoku (Medium)
# https://leetcode.com/problems/valid-sudoku/description/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.



from typing import List
# For keeping track of long the function takes to execute:
#import time 

def isValidSudoku(board: List[List[str]]) -> bool:
    #start_time = time.time()
    
    # Keep track of row and col indexes visited if there is an element at those indices. 
    # Key is the index, Value is the set containing elements that are not "."
    d_rows = {key: set() for key in range(10)}
    d_cols = {key: set() for key in range(10)}
    
    # Keep track of the subboxes in the grid
    sub_boxes = {}
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            ch = board[row][col]
            if ch != ".":
                # Check if the element already exists in the row
                if ch in d_rows[row]:
                    return False
                d_rows[row].add(ch)
                
                # Check if the element already exists in the col
                if ch in d_cols[col]:
                    return False
                d_cols[col].add(ch)
                
                # The sub-boxes are uniquely identified as a tuple using floor calculations of the rows and cols.
                # i.e sub-box (0,0) is (0,0) because row // 3 = 0, col // 3 = 0
                # In similar fashion, another subbox = (2,1) because row // 3 = 2, col // 3 = 1
                # The 9 subboxes are as follows: (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)
                curr_box = (row // 3, col // 3) # Determine which sub-box we are currently in
                # Add the subbox tuple identifier as a key to dict of all subboxes if it doesn't already exists
                if curr_box not in sub_boxes:
                    sub_boxes[curr_box] = set()

                # If the element is already present in the 3x3 sub-box
                if ch in sub_boxes[curr_box]:
                    return False
                
                sub_boxes[curr_box].add(ch)
                  
    #print("--- %s seconds ---" % (time.time() - start_time))
    return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))