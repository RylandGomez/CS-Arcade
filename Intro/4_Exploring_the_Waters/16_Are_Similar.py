def solution(a, b):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    My first approach was to iterate over each element in parallel,
    and when an inequality is found, count the instance and log the
    values. If there are more than two counts, the test autoatically
    fails in the for loop, since we cannot change three elements by
    moving two of them. Similarly, if at the end of the loop there is
    only one element, the test fails, since swapping any element pair
    could potentially fix the erroneous value, but would then replace
    a good value with a bad one. Finally, if there are two values but
    they do not resolve each other by being swapped, the test also
    fails.
    -------------------------------------------------------------------
    '''

    count = 0
    l_a = []
    l_b = []
    for i in range(0, len(a)):
        if a[i] != b[i]:
            count += 1
            if count > 2:
                return False
            l_a.append(a[i])
            l_b.append(b[i])
    if count == 1 or (count == 2 and (l_a[0] != l_b[1] or l_a[1] != l_b[0])):
        return False
    return True

def oneline(A, B):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    User kujakujaku from Vietnam utilized the sorted and sum functions
    to create a one line solution to the problem using some implicit
    logic. In order for an element swap (or lack thereof) to result in
    two identical arrays, their sorted values MUST be equal. However,
    to eliminate arrays who need more than one pair swap, the sum
    conditional must be added, which zips the two arrays and counts the
    number of inequalities within them element by element. Because the
    sorted function already removed the odd values of this count from
    consideration, we need only make sure that the total number of
    inequalities is less than or equal to 2.
    -------------------------------------------------------------------
    '''

    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2
    