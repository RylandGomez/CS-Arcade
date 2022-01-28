def solution(a):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    My first approach was creating two empy lists with a state toggle,
    and appending the corresponding values to the arrays; then
    returning their sums.
    -------------------------------------------------------------------
    '''

    state = 0
    team1 = []
    team2 = []
    for x in a:
        if state == 0:
            team1.append(x)
            state += 1
        elif state == 1:
            team2.append(x)
            state -= 1
    return [sum(team1), sum(team2)]

def slicing(a):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    This approach utilizes list slicing in format...
    list(start:stop:step) is the syntax...
    to achieve the same result in a one-liner.
    -------------------------------------------------------------------
    '''
    
    return [sum(a[::2]), sum(a[1::2])]
            