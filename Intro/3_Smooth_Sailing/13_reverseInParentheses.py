def solution(inputString):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    My solution uses a while loop to find every pair of parentheses and
    reverse them. One thing to note is that it does not matter what
    order you reverse nested parentheses, the outcome will be the same.
    In order to detect each pair, I find the first right paren and then
    find the last left paren from the start of the string to the index
    of that right paren. Then, I reconstruct the inputString using
    indexing and reverse slicing to flip the contained characters and
    omit the found parens. Once the while loop breaks, the string is
    ready to return.
    -------------------------------------------------------------------
    '''
    while ")" in inputString:
        rp = inputString.find(")")
        lp = inputString[:rp].rfind("(")
        inputString = inputString[:lp] + inputString[lp+1:rp][::-1] + inputString[rp+1:]
    return inputString

def creative(s):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    a5537 from the Russian Federation utilized a a tactic originating
    from a user named vanpet90, which is a very crafty approach to the
    problem. It utilizes Python's eval() function, which can take a
    string and run it as a line of Python code.

    IMPORTANT: Using eval() irresponsibly can create huge security
    risks in live code, so err on the side of not utilizing it unless
    you are confident in your knowledge of the repercussions.

    This solution simply replaces the parentheses with the necessary
    code add-ons to flip the substrings with a [::-1] slice. 
    ( becomes +( and ) becomes )[::-1]+.
    The result is a line of code that concatenates the substrings
    outside of the parens with the flipped substrings within the
    parens.
    See an example below for better visualization.

    "Thi(sis)ane(xa(mp)le)"
    becomes
    "Thi"+("sis")[::-1]+"ane"+("xa"+("mp")[::-1]+"le")[::-1]+""
    and for better readability
    "Thi" +("sis")[::-1] +"ane" +("xa" +("mp")[::-1] +"le")[::-1] +""
    -------------------------------------------------------------------
    '''

    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')

def recursive(s):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    User dubrov from the Russian Federation utilized recursion to
    accomplish the same functionality as my approach. They iterate over
    all characters, storing the most recently passed ( until they find
    the first ), at which point they recall the function for the string
    after flipping the found parens and omitting the parens.
    -------------------------------------------------------------------
    '''
    
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return recursive(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s