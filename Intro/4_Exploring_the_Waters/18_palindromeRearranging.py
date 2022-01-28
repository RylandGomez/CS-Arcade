def solution(inputString):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    For this problem, I created a dictionary and counted the total
    occurrences of each character within the string. I then checked if
    a palindrome could be made using the modulo operator on each value
    within the dictionary. Modulo 2 is an easy test to see if a number
    is even or odd. In a palindrome, at most one character can have an
    odd number of occurrences (in which it would be placed in the
    center of the word), so if more than one was detected, the code
    returns False. Otherwise, it returns True.
    -------------------------------------------------------------------
    '''

    cache = {}
    # count occurrences
    for c in inputString:
        if c not in cache:
            cache[c] = 1
        else:
            cache[c] += 1
    
    # check if possible
    count = 0
    for x in cache.values():
        if x % 2 == 1:
            count += 1
            if count > 1:
                return False
    return True

def solution(inputString):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    andrew_pudge from the United States condenses this functionality
    into a one liner below. By utilizing the count(substring) method
    and the set(iter) function, they iterate over each unique character
    and count the number of occurrences. This count is then reduced
    modulo 2. This resultant array is then summed into an integer whose
    value, if greater than 1, would result in a test fail, same as my
    approach.
    -------------------------------------------------------------------
    '''
    
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1