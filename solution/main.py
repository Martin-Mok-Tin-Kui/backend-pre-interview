from solver import Solver

with open('../sudoku.txt', 'r') as f:
    # init the solver
    s = Solver()

    board = []
    grid_name = ""
    
    # create and open file to write solutions to
    f2 = open('../solutions.txt', 'w') 

    for line in f:
        line = line.strip()
        if "Grid" in line:
            grid_name = line
            count = 0
        else:
            board.append([int(char) for char in line])
            count += 1
            # A board was fully read
            if count == 9:
                s.solve(board)

                # write result to file
                f2.write(grid_name + "\n")
                # write board result row by row
                for row in board:
                    row = "".join([str(x) for x in row])
                    f2.write(row+"\n")
                
                # Find the sum of the first three numbers in the top row (from the left)
                f2.write(f"sum: {str(sum(board[0][:3]))}\n")

                # finish proccessing the whole board, clear the board for next test case
                board = []

    # close the writing file once all solutions found
    f2.close()