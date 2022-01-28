def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    Since all values are in question in this problem, I sort both
    arrays, and then compare the resultant arrays.
    -------------------------------------------------------------------
    '''

    a = sorted([yourLeft, yourRight])
    b = sorted([friendsLeft, friendsRight])
    return a == b

def oneline(yourLeft, yourRight, friendsLeft, friendsRight):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    chris_l65 from the United States utilized the fact that sets are
    displayed as sorted to turn the problem into a one line solution.
    Their solution and mine vary under the hood of Python, but the end
    result in this context is the same.
    -------------------------------------------------------------------
    '''

    return {yourLeft, yourRight} == {friendsLeft, friendsRight}
