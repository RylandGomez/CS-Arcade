def solution(statues):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    Total statues is actually calculated by:
    max(statues) - (min(statues) - 1)
    but rewritten for easier readability.

    This is because max(statues) denotes the most possibly needed
    statues given the largest size. The smallest possible statue has a
    size of 1, since a size of 0 would be nonexistent, and a negative
    size unreal. Therefore, the difference of the smallest statue in
    the array and 1 will give the count of statues too small to be
    included in the arrangement. So, we take the amount of statues to
    count up to the max and subtract the statues that are smaller than
    the min. This gives us the total statues needed. Then all we do is
    subtract how many we already have from this total to return our answer.
    -------------------------------------------------------------------
    '''

    total_statues = (max(statues) - min(statues) + 1)
    current_statues = len(statues)
    return total_statues - current_statues

def condensed(statues):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    This is just an alternate one line version of the above code,
    condensed into one line.
    -------------------------------------------------------------------
    '''
    
    return max(statues) - min(statues) + 1 - len(statues)
    