def solution(inputArray):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    I slid a 2-length window over the array, comparing the absolute
    difference of each pair of elements captured within the window
    iterations, and logging the greatest value as I went.
    -------------------------------------------------------------------
    '''

    m = 0
    for i in range(0, len(inputArray) - 1):
        diff = abs(inputArray[i] - inputArray[i+1])
        if diff > m:
            m = diff
    return m

def oneline(a):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    User minh_truong from Vietnam condensed this functionality into a
    one liner below. The max() function achieves the same result as the
    conditional within my for loop by using an array consisting of the
    values I iteratively generated.
    -------------------------------------------------------------------
    '''
    
    return max([abs(a[i]-a[i+1]) for i in range(len(a)-1)])
