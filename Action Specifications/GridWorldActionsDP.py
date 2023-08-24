import sys
sys.path.append(r"C:\Users\hrida\ReinforcementLearning")
from Environments import initialize_gridWorld as gridWorld 
action_space, state_space, rewards = gridWorld()

Nr = len(state_space)
Nc = len(state_space[0])

def isValid(row, col):
    if row <0 or row>=Nr or col<0 or col>=Nc:
        return False
    return True
    
def isTerminal(row, col):
    if row == Nr-1 and col == Nc -1:
        return True
    return False

def actions(row, col, action, state_space):
    if action ==0:
        next_state = state_space[row][col-1] if isValid(row, col-1) else -1000
    if action==1:
        next_state = state_space[row][col+1] if isValid (row, col+1) else -1000
    if action ==2:
        next_state = state_space[row-1][col] if isValid (row-1, col) else -1000
    if action ==3:
        next_state = state_space[row+1][col] if isValid (row+1, col) else -1000
    return next_state

def action_tuple(row, col, action):
    if action ==0:
        next_state = (row,col-1) if isValid(row, col-1) else (row,col)
    if action==1:
        next_state = (row,col+1) if isValid (row, col+1) else (row,col)
    if action ==2:
        next_state = (row-1,col) if isValid (row-1, col) else (row,col)
    if action ==3:
        next_state = (row+1, col) if isValid (row+1, col) else (row,col)
    return next_state

def possible_actions(row, col, gamma=0.9):
    summ = 0
    for action in action_space:
        next_state = action_tuple(row, col, action)
        reward = rewards[next_state]
        next_state_value = state_space[next_state]
        net = reward + gamma * next_state_value
        summ += net
    return summ/len(action_space)
        

