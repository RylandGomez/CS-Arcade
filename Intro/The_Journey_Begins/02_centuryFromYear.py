import math

def solution(year):
    '''
    PROMPT
    -------------------------------------------------------------------
    Given a year, return the century it is in. The first century spans
    from the year 1 up to and including the year 100, the second - from
    the year 101 up to and including the year 200, etc.
    -------------------------------------------------------------------
    '''
    
    return math.ceil(year/100)
    # The math.ceil() function always rounds a float up to the nearest
    # integer and returns it.

def solution2(year):
    '''
    -------------------------------------------------------------------
    If it is desired to avoid math library, floor division can be used:
        99 is added to the year value before the floor division as
        opposed to 1 being added afterwards. This ensures proper
        calculation amongst all cases (specifically protecting against
        year % 100 = 0).
        By adding one less than the floor division value, the algorithm
        ensures an output of +1 for all values except multiples of 100.
    '''      
    return (year + 99) // 100
    