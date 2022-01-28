def solution(inputArray):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    I assign the maximum string length of the array to x, and then
    create another array from the inputArray if it is equal to that
    value.
    -------------------------------------------------------------------
    '''
    
    x = max([len(s) for s in inputArray])
    return [s for s in inputArray if len(s) == x]
    
