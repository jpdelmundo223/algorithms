"""What is Sudoku?
    - Sudoku is a logic-based, combinatorial number-placement
    puzzle. In classic sudoku, the objective is to fill a 9 x 9
    grid with digits so that each column, each row, and each 
    of the nine 3 x 3 subgrids that compose the grid contains
    all of the digits from 1 to 9
"""
# a 2D array puzzle that consists of 1 - 9 numbers.
puzzle = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

def print_board():
    """Helper function that will print the grid on a nicely 
        formatted output
    """
    global puzzle
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("---------------------------")
        for col in range(9):
            if col % 3 == 2 and col != 8:
                print(puzzle[row][col], end=" | ")
            else:
                print(puzzle[row][col], end="  ")
        print()

def is_number_valid(r, c, number):
    """Helper function that checks if the number is safe
        to place at the grids current row, column, 3 x 3 position
    """
    # checks each columns
    for col in range(9):
        if puzzle[r][col] == number:
            return False

    # checks each rows
    for row in range(9):
        if puzzle[row][c] == number:
            return False

    # checks every 3x3 rows and columns
    start_row = r - r % 3
    start_col = c - c % 3
    for row in range(3):
        for col in range(3):
            if puzzle[row + start_row][col + start_col] == number:
                return False
    
    return True

def solve(puzzle):
    """Function that will solve and render the sudoku puzzle
        Note: This function uses recursion. Python also accepts 
        function recursion, which means a defined function can call itself. 
        Recursion is a common mathematical and programming concept. 
        It means that a function calls itself. This has the benefit 
        of meaning that you can loop through data to reach a result.
    """
    for r in range(9):
        for c in range(9):
            # checks if the current position in the puzzle is equal to 0
            if puzzle[r][c] == 0:
                for number in range(1, 10):
                    # checks if the number is safe to place at the current position
                    if is_number_valid(r, c, number):
                        # r = represents the row position in the array
                        # c = represents the column position in the array
                        puzzle[r][c] = number
                        # start of recursion
                        solve(puzzle)
                        puzzle[r][c] = 0
                return
    # prints the solved puzzle
    print_board()
    
if __name__ == "__main__":
    solve(puzzle)