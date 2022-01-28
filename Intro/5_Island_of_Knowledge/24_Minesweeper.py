import numpy # library pre-imported in CodeSignal
def solution(matrix):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    The iteration is explained with comments. The complex append line
    does all of the calculations for each value. The matrix slice uses
    the predetermined min and max values for proper search size,
    creates a numpy array of all boolean values within that zone, then
    flattens them into a 1D array. These boolean values are them summed
    to identify all bombs within the vicinity (a bomb would be denoted
    with True, which equates to 1, whereas the False non-bombs would be
    0). Finally, the value of the target location is subtracted to
    exclude the counting of the bomb at the current location.
    Those calculated values are appended to a row, which is then
    appended to the overall matrix a, and then returned when done.
    -------------------------------------------------------------------
    '''

    a = []
    matrix = numpy.array(matrix)
    
    for i in range(0, len(matrix)): # iterate over rows
        # identify min and max indices to account for edges
        if i == 0:
            i_min = i
        else:
            i_min = i-1
        if i == len(matrix) - 1:
            i_max = i+1
        else:
            i_max = i+2
        
        temp = []
        for j in range(0, len(matrix[0])): # iterate over values in row
            # same min max identification as for rows above
            if j == 0:
                j_min = j
            else:
                j_min = j-1
            if j == len(matrix[0]) - 1:
                j_max = j+1
            else:
                j_max = j+2
            
            temp.append(sum(matrix[i_min:i_max, j_min:j_max].flatten()) - matrix[i][j])
        a.append(temp)
    return a


def lambdas(matrix):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    User alokbakshi from the United States implemented the same
    functionality as I did using lambda functions which provide a more
    concise, albeit harder to read, solution. It also avoids relying on
    numpy, though my answer could have been restructured to omit the
    use of numpy as well.

    The conv expression returns 1 if the indices are in range and the
    matrix value is True, otherwise it returns 0. 
    This is the bomb detector.

    The nbs expression performs an action very similar to my append
    line, wherein it applies the conv expression to all indices within
    given ranges of ii and jj.
    This is the holistic matrix creator.

    The return line uses nested list comprehensions to construct a
    matrix using the nbs lambda expression.
    -------------------------------------------------------------------
    '''

    rows = len(matrix)
    cols = len(matrix[0])
    
    conv = lambda i , j : 1 if 0 <= i < rows and 0 <= j < cols and matrix[i][j] else 0
    
    nbs = lambda i, j : sum(conv(ii, jj) for ii in range(i-1, i+2) for jj in range(j-1, j+2)) - conv(i, j)
    
    return [[nbs(i, j) for j in range(cols)]for i in range(rows)]

