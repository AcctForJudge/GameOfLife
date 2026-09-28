import random
# a nxn grid, x means alive, o means dead


class GameOfLife:
    def __init__(self, n:int, c: float= 0.8):
        self.n = n
        self.c = c
        self.grid:list[list[str]] = [["o" if random.random() < 1 - c else "x" for i in range(n)] for j in range(n)]
        
    def change_grid_pos(self, row, col, value):
        self.grid[row][col] = value

    def show_grid(self, neighbours = False):
        for g in self.grid:
            print(" ".join(g))
        print()
        if neighbours:
            for i in range(self.n):
                for j in range(self.n):
                    print(self.count_moore_neighbors(self.grid, i,j), end=" ")
                print()
                
    def count_moore_neighbors(self, x, y):
        neighbours = 0
        for i in range(-1,2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif 0 <= x + i < self.n and 0 <= y + j < self.n:
                    if self.grid[x+i][y+j] == "x":
                        neighbours += 1
                else:
                    continue
        return neighbours   
    
    def play(self, show=False):
        if show:
            self.show_grid()
        new_grid = [row[:] for row in self.grid]
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                neighbours = self.count_moore_neighbors( i, j)
                if self.grid[i][j] == "x":
                    if neighbours < 2 or neighbours > 3:
                        new_grid[i][j] = "o"
                else:
                    if neighbours == 3:
                        new_grid[i][j] = "x"
        self.grid = new_grid

