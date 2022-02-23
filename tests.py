import numpy as np
from gameOfLife import GameOfLife
        
def TC_mock_interview(debug=False):
    state0 = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]

    state1 = [
        [0,0,0],
        [1,0,1],
        [0,1,1],
        [0,1,0]
    ]


    gol = GameOfLife(state0)
    if debug:
        gol.visualize()
        print(gol.board)
    
    assert gol.get_neighbour_count(0, 1) == 1
    assert gol.get_neighbour_count(0, 0) == 1
    assert gol.get_neighbour_count(2, 2) == 2
    assert gol.get_neighbour_count(3, 1) == 3
        
    gol.update()
    if debug:
        gol.visualize()
        print(gol.board)
    assert np.array_equal(gol.board, np.array(state1))
    
    
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

    gol.simulate(2)
    
def simulate_mock():
    gol = GameOfLife([
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ])

    gol.simulate()
    
def simulate_glider():
    gol = GameOfLife([
        [0,0,1,0,0,0,0,0,0,0,0,0],
        [1,0,1,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
    ])

    gol.simulate(2)
    
def simulate_blinker():
    gol = GameOfLife([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
    ])

    gol.simulate()

if __name__ == "__main__":
    TC_mock_interview()
    simulate_glider()