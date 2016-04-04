# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------

from copy import deepcopy
import math

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    # Iterative smoothing
    outside_tol = True
    while (outside_tol):
        count +=1
        outside_tol = False
        
        for i in range(1,len(path) - 1):
            
            #cache previous value
            previous_val = newpath[i]
            
            #update newpath
            data_term = [path[i][0] - newpath[i][0], path[i][1] - newpath[i][1]]
            smooth_term = [newpath[i+1][0] + newpath[i-1][0] - 2 * newpath[i][0], newpath[i+1][1] + newpath[i-1][1] - 2 * newpath[i][1]]
            newpath[i] = [newpath[i][0] + weight_data*(data_term[0]) + weight_smooth*(smooth_term[0]), newpath[i][1] + weight_data*(data_term[1]) + weight_smooth*(smooth_term[1])]
            
            #check tolerance
            this_tol = math.sqrt(math.pow(newpath[i][0] - previous_val[0],2) + math.pow(newpath[i][1] - previous_val[1],2))
            if (this_tol > tolerance):
                outside_tol = True
    
    return newpath # Leave this line for the grader!

printpaths(path,smooth(path))
