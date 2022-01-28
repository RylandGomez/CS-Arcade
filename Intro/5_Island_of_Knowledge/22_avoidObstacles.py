def solution(inputArray):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    To solve this problem, I iterated over the possible values of the
    jump from least to greatest, and tested each one's viability. If
    a test failed, I incremented the jump by a length of 1 and
    restarted the test. The test passes once the maximum value of the
    array is passed (in other words, the last obstacle has been passed)
    -------------------------------------------------------------------
    '''
    count = 0
    step = 2
    while count < max(inputArray):
        count += step
        if count in inputArray:
            count = 0
            step += 1
    return step


def solution(inputArray):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    hrithik_sql from the United States utilized the modulo operator to
    condense the code required, and likely the speed of the code though
    I haven't tested it. They utilize the all() function that returns
    true if all contained booleans are true; then they use modulo to
    discern whether or not an obstacle will be landed on. If the object
    reduced modulo the step size is zero, the object will be landed on.
    If a collision occurs, the step size grows by one, and the test
    infinitely repeats until it passes. The infinite loop is acceptable
    because in a worst case scenario, it will still break once the step
    size reaches the length needed to leap the entire array at once.
    -------------------------------------------------------------------
    '''
    
    step = 2
    while True: # infinite loop
        if all(x % step !=0 for x in inputArray):
            return step
        step += 1
            



