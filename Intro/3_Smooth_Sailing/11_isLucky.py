def solution(n):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    This is my solution, expanded for understandability. I convert n to
    a string, then turn this into an array. I identify the midpoint of
    the number, then separate it into halves. Finally, I compare the
    sums and return the proper boolean. This is a fairly messy solution
    that I clean up below.
    -------------------------------------------------------------------
    '''

    s = str(n)
    l = [int(x) for x in s]
    half = int(len(l) / 2)
    first_half = l[0:half]
    second_half = l[-1:(half*-1) - 1:-1]
    
    if sum(first_half) == sum(second_half):
        return True
    else:
        return False

def cleaner(n):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    I utilize floor division instead of int() to find a midpoint (m). I
    also remove the ridiculous slicing used in the second_half above.
    I condensed the conversion from string to integer in the list
    comprehensions for l and r (left and right). Then, I return the
    boolean asked for.
    -------------------------------------------------------------------
    '''

    s = str(n)
    m = len(s)//2
    l, r = [int(c) for c in s[:m]], [int(c) for c in s[m:]]
    return sum(l) == sum(r)