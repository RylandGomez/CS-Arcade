def solution(inputArray):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    This solution slides a 2-length window over the array, comparing
    successive value pairs. If the first value is greater than the
    second, it adds the necessary amount of moves to the counter and
    assigns the new value to the proper window location. It ends by
    returning the moves count.
    -------------------------------------------------------------------
    '''

    a = inputArray
    temp = None
    moves = 0
    for i in range(0, len(a) - 1):
        if temp != None and temp > a[i]:
            c = temp
        else:
            c = a[i]
        if c >= a[i+1]:
            moves += c - a[i+1] + 1
            temp = c + 1
            
    return moves