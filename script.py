from Puzzle import Puzzle

def main():
    puzzle = Puzzle()
    puzzle.print_board()
   
    puzzle.solve()
    print()
    puzzle.print_board()
    

if __name__ == "__main__":
    main()
