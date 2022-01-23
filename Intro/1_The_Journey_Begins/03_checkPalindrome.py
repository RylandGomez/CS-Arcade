def solution(inputString):
    '''
    PROMPT
    -------------------------------------------------------------------
    Given the string, check if it is a palindrome.
    A palindrome is a string that doesn't changed when reversed (it
    reads the same backward and forward).
    -------------------------------------------------------------------
    '''

    # Slice of [::-1] implies a start to finish slice of -1 steps 
    # (going backwards through the string). This is the reversed string.
    
    return inputString == inputString[::-1]

def alternate(inputString):
    '''
    -------------------------------------------------------------------
    An alternate method is to iterate through the string, comparing the
    first character to the last one, then the second to the character
    before the last one, and so on. This is demonstrated below.
    -------------------------------------------------------------------
    '''

    # len(inputString) // 2 is used to iterate over the first half.
    # The inputString[-1 - i] uses this iteration to reference the back
    # half of the string simultaneously. If they do not match, the
    # algorithm returns False, breaking the loop. If the loop finishes
    # without breaking, the algorithm returns True.

    for i in range(len(inputString) // 2):
        if inputString[i] != inputString[-1 - i]:
            return False
    return True
    