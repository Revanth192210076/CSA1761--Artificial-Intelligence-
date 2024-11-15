class VacuumCleaner:
    def __init__(self, grid, start):
        
        self.grid = grid
        self.position = start
        self.cleaned_cells = []

    def display_grid(self):

        for row in self.grid:
            print(row)
        print()

    def clean(self):

        rows = len(self.grid)
        cols = len(self.grid[0])

        print("Initial grid:")
        self.display_grid()

        # Traverse each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # Move to the new position
                self.position = (i, j)
                # Check if the cell is dirty
                if self.grid[i][j] == 1:
                    # Clean the cell
                    print(f"Cleaning cell at position {self.position}")
                    self.grid[i][j] = 0
                    self.cleaned_cells.append(self.position)
                    self.display_grid()
                else:
                    print(f"Cell at position {self.position} is already clean")

        print("Final grid:")
        self.display_grid()
        print("Cells cleaned:", self.cleaned_cells)

# Example Usage
# 1 represents a dirty cell, 0 represents a clean cell
grid = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

# Starting position of the vacuum cleaner (top-left corner)
start_position = (0, 0)

# Initialize and run the vacuum cleaner
vacuum = VacuumCleaner(grid, start_position)
vacuum.clean()
