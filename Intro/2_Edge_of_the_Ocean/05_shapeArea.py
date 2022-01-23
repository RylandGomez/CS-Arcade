def solution(n):
    '''
    PROMPT
    -------------------------------------------------------------------
    A 1-interesting polygon is just a square with a side of length 1.
    An n-interesting polygon is obtained by taking the
    (n - 1)-interesting polygon and appending 1-interesting polygons to
    its rim, side by side.
    -------------------------------------------------------------------
    EXPLANATION
    -------------------------------------------------------------------
    In each iteration of n-interesting polygons, we are interested in
    covering all open faces with new squares. The base case is n=1 with
    a single square and 4 open faces. Then n=2 with 4 new squares
    (total 5) and 8 new open faces (12 total). Then n=3 with 8 new
    squares (total 13) and 8 new open faces (20 total). In each
    iteration, 4 open faces must be individually covered by a new
    square, and each additional square can cover two open faces each.
    Thus, to cover 20 open faces for n=4, we need ((20-4)/2) + 4, or 12
    more squares, which will then add another 8 new open faces. 8 new
    open faces = 4 more squares every iteration, therefore although the
    jump from n=1 to n=2 and afterwards to n=3 cover a different amount
    of faces proportional to squares, the total squares added remains
    the same. So, we only need a base case of n=1.

    In other words:
    n=1 is 1
    n=2 is 1 + 4 = 5
    n=3 is 5 + (4 + 4) = 13
    n=4 is 13 + (4 + 4 + 4) = 25
    n=x is previous value + (4 * (n-1))
    -------------------------------------------------------------------
    '''
    if n==1:
        return 1 # base case
    return ((n-1)*4) + solution(n-1) # recursion

def formula(n):
    '''
    -------------------------------------------------------------------
    However, a formula can be established using RREF...

    return 1 - (2*n) + (2*(n**2))

    and this can be rewritten into a reader-friendly formula used below
    -------------------------------------------------------------------
    ''' 
    return n**2 + (n-1)**2
