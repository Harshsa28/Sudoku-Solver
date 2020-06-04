# Sudoku-Solver
The program solves sudoku via depth first search

The program takes as input a 9x9 2 dimensional list indicating the board
Then it solves it via DFS, and returns the solved board using Python library tabulate

The idea used is it first calculates all the possible values in the empty cells. And then it starts the DFS method repeatedly until it gets the correct solution, or no solution.

This method is more effective than backtracking. The time taken to solve one of the toughest sudoku problems out there is 30 milliseconds. 
