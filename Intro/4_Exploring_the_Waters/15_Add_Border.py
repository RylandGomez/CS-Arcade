def solution(picture):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    I define asts to be a line of asterisks the same length as the
    strings within picture, then include them to the start and end of
    the array picture. I then return a list comprehension that adds an
    asterisk to either side of each nested list (which could be seen as
    rows).
    -------------------------------------------------------------------
    '''
    
    asts = "*"*len*picture[0]
    picture.insert(0, asts)
    picture.append(asts)
    return ["*" + row + "*" for row in picture]
