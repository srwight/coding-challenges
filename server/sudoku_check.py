'''
This module checks a sudoku board to see if it is a valid board.

It receives a list of lists that represent the rows of the board.
It returns True if the board is a valid Sudoku Board.
'''
import numpy as np

def check_shape_contents(list_in:list) -> bool:
    check = [1,2,3,4,5,6,7,8,9,' ']
    check_string = '123456789 '
    
    # Are all of the cells' contents valid entries?
    if any(any(cell not in check and cell not in check_string for cell in row) for row in list_in):
        return False
    
    # Are there 9 rows?
    if len(list_in) != 9:
        return False
    
    # Does each row have 9 columns?
    if any(len(row) != 9 for row in list_in):
        return False

    return True

def preprocess(list_in:list) -> np.array:
    '''
    This function accepts a nested list of lists or a list of strings (list_in).
    It converts it to a numpy array of integers and nans.

    Arguments:
    ==========
    list_in (list): List of nested lists or a list of strings. Must have length of nine,
                    and each member must have a length of nine.

    Returns:
    ========
    numpy array representing the board
    '''
    
    # Convert string inputs to integers
    list_array = list(map(lambda row:[int(str(a)) if str(a).isnumeric() else np.nan for a in row], list_in))

    # Convert the input to a 2d numpy array
    return np.array(list_array)

def stack_squares(array_in:np.array) -> np.array:
    '''
    This function reshapes the array such that the 9 subsquares become 9 rows.

    Arguments:
    array_in (numpy array): numpy array representation of a sudoku board

    Returns:
    reshaped np.array 
    '''
    layer_list = []
    # Iterate through the 9 boxes and add them to the list
    for i in range(0,7,3):
        for j in range (0,7,3):
            layer_list.append(array_in[i:i+3,j:j+3].flatten())

    return np.stack(layer_list)

def check_segment(array_in:np.array) -> bool:
    '''
    This function checks a numpy array to be sure it has no repeated cells

    Arguments:
    array_in (numpy array): numpy array representation of a sudoku row or column

    Returns:
    True if each item in the array is unique
    '''

    return np.all(np.unique(array_in, return_counts=True)[1] == 1) or np.unique(array_in).size == 0

def sudoku_check(list_in:list) -> bool:
    '''
    This function accepts a list of strings or
    a nested list of lists (input). It:
        Sends the list to be checked for shape and content
        Sends the list to be converted to a numpy array
        Sends the numpy array to be reshaped to check the subsquares

        Sends each segment to be checked

        Returns true if every check returns true.

    Arguments:
    ==========
    list_in - List of lists. Must have a length of 9, and each inner list must be of length 9.

    Returns:
    ========
    True if the board is a valid sudoku puzzle
    False if the board is not a valid sudoku puzzle
    '''
    if not check_shape_contents(list_in):
        return False
    
    board = preprocess(list_in)
    board_flat = stack_squares(board)

    rows_ok = np.all(np.apply_along_axis(check_segment,0,board))
    cols_ok = np.all(np.apply_along_axis(check_segment,1,board))
    sqrs_ok = np.all(np.apply_along_axis(check_segment,1,board_flat))

    return rows_ok and cols_ok and sqrs_ok
    