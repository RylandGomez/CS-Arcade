def solution(sequence):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    To solve this problem, I created a window of length 3 to scan the
    array and implemented conditionals to detect necessary removals and
    modify the window scanning process as needed. 
    In short, the iterated elements always constitute the last value,
    while the two previous values are modified manually as needed.
    Comments are added to make all actions explicit.
    -------------------------------------------------------------------
    '''

    # window structure is [a, b, element]
    # Set all previous elements lower than minimum value
    a = b = min(sequence) - 1 

    removed = False # default to 0 removals
    
    for element in sequence:
        # Uncomment the below line for console printouts of the window
        # scanning process (helpful for visual understanding).

        # print(f'[{a}, {b}, {element}]')

        if element <= b: # element larger than previous value
            # Removal check
            if removed:
                return False # 2 removals terminates test
            else:
                removed = True # 1 removal logged

            # Conditional manipulation of window
            if element <= a: # element is issue, larger than both
                continue # previous values unchanged
            elif element > a: # b is issue as b >= element > a
                b = element # import element into b value to create
                            # new window

        else: # no issue found
            a, b = b, element # shift previous values in window

    # If iteration doesn't return False, tests pass with 1 or fewer
    # removals.
    return True
    