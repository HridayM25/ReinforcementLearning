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
    
    Actions Space : 
    
    0 -> Left
    1 -> Right 
    2 -> Upwards
    3 -> Downwards
    
    """
    ROWS = rows 
    COLUMNS = columns
    WIND = int(COLUMNS//2)
    no_of_actions = 4
    action_space = [0, 1, 2, 3]
    Qtable = np.zeros((ROWS*COLUMNS, no_of_actions))
    rewards = np.ones((ROWS*COLUMNS, no_of_actions)) * -1
    return WIND, Qtable, rewards, action_space