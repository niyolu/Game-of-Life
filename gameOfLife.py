import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

class GameOfLife:
    def __init__(self, board):
        self.board = np.array(board)
        self.n, self.m = self.board.shape
        
    def update(self):
        changes = []
        
        for row in range(self.n):
            for col in range(self.m):
                neighbour_count = self.get_neighbour_count(row, col)
                state = self.board[row, col]
                state_change = self.apply_rules(state, neighbour_count)
                if state_change:
                    changes.append((row, col))
        
        for row, col in changes:
            self.swap(row, col)
            
    def is_alive(self, row, col):
        if row in (-1, self.n) or col in (-1, self.m):
            return 0
        return self.board[row, col]
                
    
    def get_neighbour_count(self, row, col):
        idxs = ((row + i, col + j) for i in (0, 1, -1) for j in (0, 1, -1) if not i == j == 0)
        count = sum(self.is_alive(*idx) for idx in idxs)
        return count
    
    def apply_rules(self, state, neighbour_count):
        alive = state == 1
        death = alive and not neighbour_count in (2, 3)
        birth = not alive and neighbour_count == 3
        return death or birth
    
    def swap(self, row, col):
        self.board[row][col] ^= 1
        
    def visualize(self):
        plt.imshow(self.board, cmap="binary")
        plt.show()
        
    def simulate(self, generation_decades=1):
        # matplot magic stolen from https://stackoverflow.com/a/55876734
        ax_rows = 10 * generation_decades // 5
                
        Z = self.board

        X, Y = np.meshgrid(np.arange(Z.shape[1])+.5, np.arange(Z.shape[0])+.5)

        fig, axes = plt.subplots(ax_rows, 5, figsize=(16, 8))
        for i, ax in enumerate(axes.flat):
            ax.scatter(X[Z > 0], Y[Z > 0], color="k")

            ax.grid(True, color="k")
            ax.xaxis.set_major_locator(mticker.MultipleLocator())
            ax.yaxis.set_major_locator(mticker.MultipleLocator())
            ax.tick_params(size=0, length=0, labelleft=False, labelbottom=False)
            ax.set(xlim=(0, Z.shape[1]), ylim=(Z.shape[0], 0),
                title=f'Generation {i+1}', aspect="equal")
            
            self.update()

        plt.tight_layout()
        plt.show()
