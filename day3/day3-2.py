# imports

# open import file
with open('day3/input', 'r') as input:
    inputgrid = [line for line in input.read().splitlines()]


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.number_of_rows = len(self.grid)
        if max([len(row) for row in grid]) != min([len(row) for row in grid]):
            raise ValueError("Row lengths do not match")
        else:
            self.number_of_columns = len(self.grid[0])
    
    def get_coord(self, x_coord, y_coord, wrap=False):
        if wrap==True:
            return self.grid[y_coord][x_coord % self.number_of_columns]
        else:
            return self.grid[y_coord][x_coord]

    def traverse(self, start_coord:tuple, x_movement, y_movement, search_character, check_first=False):
        """
        start_coord tuple should be in form (x,y) with top left being (0,0).
        
        x_movement = movement right per step

        y_movement = movement down per step

        search_character = character to find in the grid

        check_first = whether to check for search_character in start_coord
        """
        self.pointer = list(start_coord)
        characters_found = 0
        if check_first == True:
            if self.get_coord(self.pointer[0], self.pointer[1], wrap=True) == search_character:
                characters_found += 1
        while self.pointer[1] < self.number_of_rows - 1:
            self.pointer[0] += x_movement
            self.pointer[1] += y_movement
            if self.get_coord(self.pointer[0], self.pointer[1], wrap=True) == search_character:
                characters_found += 1
        return characters_found


my_grid = Grid(inputgrid)
test1 = my_grid.traverse((0,0),1,1,'#')
test2 = my_grid.traverse((0,0),3,1,'#')
test3 = my_grid.traverse((0,0),5,1,'#')
test4 = my_grid.traverse((0,0),7,1,'#')
test5 = my_grid.traverse((0,0),1,2,'#')

print(test1, test2, test3, test4, test5)
print(test1 * test2 * test3 * test4 * test5)
