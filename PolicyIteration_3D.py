# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    
    default_str = ' '
    policy3D = [[[default_str for row in range(len(grid[0]))] for col in range(len(grid))],
             [[default_str for row in range(len(grid[0]))] for col in range(len(grid))],
             [[default_str for row in range(len(grid[0]))] for col in range(len(grid))],
             [[default_str for row in range(len(grid[0]))] for col in range(len(grid))]]

    
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    change = True
    while(change):
        change = False

        for x in range(len(grid)): 
            for y in range(len(grid[0])):
                for d in range(len(forward)):

                    #if goal state
                    if (goal[0] == x and goal[1] == y):
                        if (value[d][x][y] > 0):
                            change = True
                            policy3D[d][x][y] = '*'
                            value[d][x][y] = 0
                        
                    #if regular square
                    elif (grid[x][y] == 0):
                        for a in range(len(action)):
                            d2 = (d + action[a])%4
                            x2 = x + forward[d2][0]
                            y2 = y + forward[d2][1]
                            
                            if ((x2 < len(grid)) and (x2 > -1) and (y2 < len(grid[0])) and (y2 > -1) and (grid[x2][y2] == 0)):
                                new_val = value[d2][x2][y2] + cost[a]
                                if (new_val < value[d][x][y]):
                                    value[d][x][y] = new_val
                                    policy3D[d][x][y] = action_name[a]
                                    change = True                      
    
    ### Iterate through Policy3D to get Policy2D   
    loc = init
    reached_goal = False
    while (not reached_goal):

        d = loc[2]
        x = loc[0]
        y = loc[1]
        
        policy = policy3D[d][x][y]
        policy2D[x][y] = policy
        

        if (policy == '*'):
            reached_goal = True
        elif (policy == '#'):
            d2 = d
        elif (policy == 'R'):
            d2 = (d - 1)%4
        elif (policy == 'L'):
            d2 = (d + 1)%4
            
        x2 = x + forward[d2][0]
        y2 = y + forward[d2][1]    
 
        loc = [x2, y2, d2]
    
    for i in range(len(policy2D)):
        print policy2D[i]
        
    return policy2D  

optimum_policy2D(grid,init,goal,cost)