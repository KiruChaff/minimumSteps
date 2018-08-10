import sys
matrix = [[False, False, False, False],\
        [True, True, False, True],\
        [False, False, False, False],\
        [False, False, False, False]]

## MAIN--INPUT START/END-TUPLES
def minimumSteps(start, end):
    ## CALLS COMPUTING FUNCTION--CONVERTING START INTO X AND Y
    return getMinSteps(start[1], start[0], end)

## COMPUTING FUNCTION
def getMinSteps(x, y, end, steps=0, memo={}):
    ## BASE CASE
    if (x==end[1] and y==end[0]):
        return steps
    ## CHECKS IF COORDINATES ARE STILL IN RANGE
    if ( x>=0 and y>=0 and y<len(matrix) and x<len(matrix[y])):
        x_y = str(x)+"_"+str(y)
        ## CHECKS IF POSITION GOT COMPUTED ALREADY--AVOIDS CYCLES
        if (x_y in memo):
            if (memo[x_y]<steps):
                return sys.maxsize
        ## IN CASE POSITION IS 'False'(VALID)
        if (not matrix[y][x]):
            memo[x_y]=steps
            steps+=1
            ## MOVES IN EVERY POSSIBLE DIRECTION--CHOSES MOST EFFICIENT OUTCOME
            result = min(\
            getMinSteps(x + 1, y, end, steps, memo),\
            getMinSteps(x - 1, y, end, steps, memo),\
            getMinSteps(x, y + 1, end, steps, memo),\
            getMinSteps(x, y - 1, end, steps, memo))
            return result
    return sys.maxsize

## ----------------------------------------------------------- ##

print(minimumSteps((3, 0), (0, 0)))

## >>> 7
