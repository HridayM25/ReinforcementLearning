
import sys
sys.path.append(r"C:\Users\hrida\ReinforcementLearning")
from Environments import initialize_windyGridworld as gridWorld

WIND, Qtable, rewards, action_space, rows, cols = gridWorld(4,6)

ROWS =cols
COLS = rows

def inBounds(state, action,ROWS,COLS):
    if action==0 and state%ROWS==0:
        return False
    if action==1 and (state+1)%ROWS==0:
        return False
    if action ==2:
        if state>=0 and state<=ROWS -1:
            return False
    if action==3:
        if state>=ROWS*(COLS-1) and state<=(ROWS*COLS)-1:
            return False
    return True
    

def actions(state, action,ROWS,COLS):
    if (state-2) % ROWS ==0:
        state = state - ROWS if inBounds(state, 2,ROWS, COLS) else state
    if action==0:
        next_state = state-1 if inBounds(state,action,ROWS, COLS) else state
    if action ==1:
        next_state = state+1 if inBounds(state, action,ROWS, COLS) else state
    if action ==2:
        next_state = state-ROWS if inBounds(state, action,ROWS, COLS) else state
    if action == 3:
        next_state = state+ROWS if inBounds(state,action, ROWS, COLS) else state 
    return next_state




