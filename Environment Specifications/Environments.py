import numpy as np 
import pandas as pd


def initialize_randomwalk(states=19):
  STATES = states
  value_list = np.zeros(STATES)
  state_check = np.zeros(STATES)
  rewards = np.zeros(STATES)
  rewards[0] = -1
  rewards[STATES-1] = 1
  start_pos = (STATES+1)/2 -1
  action_space = [-1, 1]
  return value_list, state_check, int(start_pos), rewards, action_space


def initialize_windyGridworld(rows, columns):
    """
    0 0 0 0 0 . . . W 0 0 0 0 . . . . 
    0 0 0 0 0 . . . W 0 0 0 0 . . . . 
    0 0 0 0 0 . . . W 0 0 0 0 . . . . 
    0 0 0 0 0 . . . W 0 0 0 0 . . . . 
    0 0 0 0 0 . . . W 0 0 0 0 . . . . 
    0 0 0 0 0 . . . W 0 0 0 0 . . . . 
    . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . . 
    
    The column in the middle of the GridWorld has some wind associated with it, in the upwards direction. 
    For example, if you take a step to the left when you are present in the column, you will end up in a state up, and to the left of
    the current state. 
    
    Action Space : 
    
    0 -> Left
    1 -> Right 
    2 -> Upwards
    3 -> Downwards
    
    Rewards :
    
    -1 for each move 
    +10 if you escape (last element of the GridWorld)
    
    """
    ROWS = rows
    COLS = columns
    WIND = int(COLS//2)
    no_of_actions = 4
    action_space = [0, 1, 2, 3]
    Qtable = np.zeros((ROWS*COLS, no_of_actions))
    rewards = np.ones((ROWS*COLS)) * -1
    rewards[-1]=10
    return WIND, Qtable, rewards, action_space, ROWS, COLS

def initialize_gridWorld(rows =4, cols =4):
    actions=4
    action_space = [0,1,2,3]
    state_space = np.zeros((rows,cols))
    rewards = np.ones((rows, cols)) *-1
    rewards[rows-1][cols-1] = 10
    return action_space, state_space, rewards