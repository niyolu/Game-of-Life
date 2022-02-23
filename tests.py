from re import M, X
import numpy as np
from gameoflife import GameOfLife


def TC_mock_interview(debug=False):
    # https://www.youtube.com/watch?v=T9Y82JH4-pY&t=450s

    state0 = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    state1 = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ]

    gol = GameOfLife(state0)

    if debug:
        gol.visualize()
        print(gol.grid)

    assert gol.get_neighbour_count(0, 1) == 1
    assert gol.get_neighbour_count(0, 0) == 1
    assert gol.get_neighbour_count(2, 2) == 2
    assert gol.get_neighbour_count(3, 1) == 3

    gol.update()

    if debug:
        gol.visualize()
        print(gol.grid)

    assert np.array_equal(gol.grid, np.array(state1))


def simulate_beehive():
    gol = GameOfLife([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    gol.simulate()


def simulate_mock():
    gol = GameOfLife([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ])

    gol.simulate()

def simulate_glider():

    glider = [[0, 0, 1],
           [1, 0, 1],
           [0, 1, 1]]
    
    gol = GameOfLife(glider, (12, 12))

    gol.simulate(3)

def simulate_blinker():
    gol = GameOfLife([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ])

    gol.simulate()

if __name__ == "__main__":
    TC_mock_interview()
    simulate_glider()
   