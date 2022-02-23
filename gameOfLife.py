import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


class GameOfLife:
    def __init__(self, grid, dim=None):
        self.grid = GameOfLife.prepare_grid(grid, dim)
        self.n, self.m = self.grid.shape

    def update(self):
        changes = []

        for row_idx, row in enumerate(self.grid):
            for col_idx, cell_state in enumerate(row):
                neighbour_count = self.get_neighbour_count(row_idx, col_idx)
                state_change = self.apply_rules(cell_state, neighbour_count)
                if state_change:
                    changes.append((row_idx, col_idx))

        for row, col in changes:
            self.swap(row, col)

    def is_alive(self, row, col):
        if row in range(self.n) and col in range(self.m):
            return self.grid[row, col]
        return 0

    def get_neighbour_count(self, row, col):
        idxs = ((row + i, col + j)
                for i in (0, 1, -1)
                for j in (0, 1, -1)
                if not i == j == 0)
        count = sum(self.is_alive(*idx) for idx in idxs)
        return count

    def apply_rules(self, state, neighbour_count):
        alive = state == 1
        death = alive and not neighbour_count in (2, 3)
        birth = not alive and neighbour_count == 3
        return death or birth

    def swap(self, row, col):
        self.grid[row][col] ^= 1

    def visualize(self, X, Y, ax, gen):
        # matplot magic stolen from https://stackoverflow.com/a/55876734
        ax.scatter(X[self.grid > 0], Y[self.grid > 0], color="k")
        ax.grid(True, color="k")
        ax.xaxis.set_major_locator(mticker.MultipleLocator())
        ax.yaxis.set_major_locator(mticker.MultipleLocator())
        ax.tick_params(size=0, length=0, labelleft=False,
                       labelbottom=False)
        ax.set(xlim=(0, self.m), ylim=(self.n, 0),
               title=f'Generation {gen + 1}',
               aspect="equal")

    def simulate(self, generation_decades=1):
        ax_rows = 10 * generation_decades // 5
        fig, axes = plt.subplots(ax_rows, 5, figsize=(16, 8))
        X, Y = np.meshgrid(
            np.arange(self.m) + .5, np.arange(self.n) + .5)
        for gen, ax in enumerate(axes.flat):
            self.visualize(X, Y, ax, gen)
            self.update()

        plt.tight_layout()
        plt.show()

    @classmethod
    def prepare_grid(cls, grid, dim):
        if not isinstance(grid, np.ndarray):
            grid = np.array(grid)
        if dim and dim != grid.shape:
            grid = np.pad(grid, mode="constant", pad_width=(
                (0, dim[0] - grid.shape[0]), (0, dim[1] - grid.shape[1])))
        return grid
