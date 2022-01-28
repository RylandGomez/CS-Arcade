import math

def solution(year):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    The math.ceil() function always rounds a float up to the nearest
    integer and returns it. This is utilized to ensure the
    encapsulating century is returned.
    -------------------------------------------------------------------
    '''
    
    return math.ceil(year/100)
    

def alternate(year):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    If it is desired to avoid math library, floor division can be used:
        99 is added to the year value before the floor division as
        opposed to 1 being added afterwards. This ensures proper
        calculation amongst all cases (specifically protecting against
        year % 100 = 0).
        By adding one less than the floor division value, the algorithm
        ensures an output of +1 for all values except multiples of 100.
    -------------------------------------------------------------------
    '''
          
    return (year + 99) // 100
    