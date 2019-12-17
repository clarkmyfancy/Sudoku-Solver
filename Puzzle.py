class Puzzle:

    def __init__(self):
        self.is_not_solved = True
        
        self.grid = [
                [8, 0, 0, 4, 0, 0, 5, 0, 0],
                [2, 6, 0, 0, 0, 9, 0, 1, 0],
                [4, 0, 0, 0, 0, 0, 0, 0, 7],
                [0, 0, 0, 0, 4, 5, 6, 2, 0],
                [0, 0, 0, 0, 7, 0, 0, 0, 0],
                [0, 2, 4, 3, 9, 0, 0, 0, 0],
                [7, 0, 0, 0, 0, 0, 0, 0, 3],
                [0, 8, 0, 7, 0, 0, 0, 4, 1],
                [0, 0, 5, 0, 0, 8, 0, 0, 2]
            ]

        

    # def generate_alternative_numbers_for(self, grid):
    #     pass

    def choose_number_to_try_here(self):
        # need to check remaining possible choices for this number
        # if reminin g choices get exhausted:
        pass

    def print_board(self):
        for x in range(9):
            print(self.grid[x])
            print()

    def attempt_to_solve(self):
        pass

    def generate_candidate_answers():
        self.candidate_answers = generate_candidate_answers()
        pass