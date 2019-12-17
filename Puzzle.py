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

    def print_board(self):
        for x in range(9):
            print(self.grid[x])

    def solve(self):
        found_empty_box_location = self.find_empty_box()
        if not found_empty_box_location:
            return True
        else: 
            row, column = found_empty_box_location

        for candidate in range(1, 10):
            if self.valid_candidate_for_position(candidate, (row, column)):
                self.grid[row][column] = candidate

                if self.solve():
                    return True 
            
                self.grid[row][column] = 0
        return False

    def find_empty_box(self):
        for row in range(9):
            for column in range(9):
                if self.grid[row][column] == 0:
                    return (row, column)
        return None
    
    def valid_candidate_for_position(self, candidate, position):
        if self.passed_horizontal_rule(candidate, position) and self.passed_vertical_rule(candidate, position) and self.passed_neighbor_rule(candidate, position):
            return True
        return False
    
    def passed_horizontal_rule(self, candidate, position):
        for i in range(9):
            if self.grid[position[0]][i] == candidate and position[1] != i:
                return False
        return True
        
    def passed_vertical_rule(self, candidate, position):
        for i in range(9):
            if self.grid[i][position[1]] == candidate and position[0] != i:
                return False
        return True
        
    def passed_neighbor_rule(self, candidate, position):
        box_x = position[1] // 3
        box_y = position[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.grid[i][j] == candidate and (i, j) != position:
                    return False
        return True