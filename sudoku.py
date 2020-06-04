import collections
from tabulate import tabulate
import time

def solve(sudoku):
    def possibilities():
        #shows all the possible values for every single empty cell in the sudoku
        d, unfill = collections.defaultdict(list), set()
        for i, r in enumerate(sudoku):
            for j, e in enumerate(r):
                if e != ".":
                    d[("r", i)] += [e]
                    d[("c", j)] += [e]
                    d[(i // 3, j // 3)] += [e]
                else:
                    unfill.add((i, j))
        return {(i, j): list(set("123456789") - set(d[("r", i)] + d[("c", j)] + d[(i // 3, j // 3)])) for i, j in unfill}

    def dfs():
        def checker(num, i, j, update): #num is number to try, i,j are indices, update is all possiblities
            sudoku[i][j] = num   #try number on the board
            del val[(i, j)]     #if we have number in board, its not needed in val as that cell is not empty anymore
            for (m, n), v in val.items():   #m, n are indices, and v is all possibilities at those indices     
                if num not in v or not( m == i or n == j or (m // 3, n // 3) == (i // 3, j // 3)): continue   #if there's no one in vicinity and number not in possibilities, try next one to check again.
                update[(m, n)] = num  #showinf that we removed number from (m,n). So that if we are wrong, we can add it later
                v.remove(num)  #because number is in possibilites in vicinity, we have to remove the number from the possibilities
                if len(v) == 0: return False  #if we removed all possibilities, then obviously our assumption is False
            return True  #the assumption didn't ruin anything, so FOR NOW we assume that our assumption will work and go deeper with DFS

        if len(val) == 0: return True #if len(val) == 0, then the board has no missing cells, so just return True, no need to implement DFS
        cur = min(val.keys(), key=lambda x: len(val[x])) #finds the cell with the minimum NUMBER of possibilities. Like said in Sudoku Solver by Google guy
        for num in val[cur]:  #iterates through possibilities of smallest empty cell
            update = {cur: val[cur]}    
            if checker(num, cur[0], cur[1], update) and dfs(): return True   #this is where we actually implement depth first search. We assume something and go deeper and deeper. It's effective. If it does return True, then that means that it went deep all the way and there was no fault. So sudoku at this level is solved. So we return True. 
            sudoku[cur[0]][cur[1]] = "."  #if above statement is False, then obviously our assumption is False, and therefore board[loc] = "."
            for k in update: val[k] += update[k]   #now, we know our assumption was wrong. So we replace all the numbers we deleted. 
        return False    #if all possibilities we checked are wrong, then the assumption is previous layer was wrong, and so we return False

    val = collections.defaultdict(list)
    val.update(possibilities())
    dfs()
    return sudoku

board = [['.','.','9','.','3','2','.','.','.'],
        ['.','.','.','7','.','.','.','.','.'],
        ['1','6','2','.','.','.','.','.','.'],
        ['.','1','.','.','2','.','5','6','.'],
        ['.','.','.','9','.','.','.','.','.'],
        ['.','5','.','.','.','.','1','.','7'],
        ['.','.','.','.','.','.','4','.','3'],
        ['.','2','6','.','.','9','.','.','.'],
        ['.','.','5','8','7','.','.','.','.']]

start = time.time()
print(tabulate(solve(board)))
end = time.time()
print("time taken is :", end-start)
