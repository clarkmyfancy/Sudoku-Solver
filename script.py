from Puzzle import Puzzle



def main():

    

    # rules = ?
    puzzle = Puzzle()

    puzzle.print_board()
   
    
    # while there is more board to solve
        # pick new number to try in current location
        # if it violates rule, 
            # pick new number from the set of remaingin possible choices 
        # if run out of elements in the set of possible choices
            # backtrack to last candidate_sqare and repick their answer
    while puzzle.is_not_solved:
        puzzle.attempt_to_solve()
        for y in range(len(candidate_puzzle)):
            for x in range(len(candidate_puzzle[y])):
                puzzle.choose_number_to_try_here()
             
                   
                        # __
                    number = candidate_puzzle[x][y]
        board_is_not_solved = False


if __name__ == "__main__":
    main()
