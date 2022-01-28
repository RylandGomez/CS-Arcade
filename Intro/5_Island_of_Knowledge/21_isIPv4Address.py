def solution(inputString):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    To approach this problem, I first separate the string on each ".".
    This allows me to check the various attributes of an IP address.
    First, if this does not result in four substrings, the IP address
    is invalid. Following that, I must check each substring for various
    qualities. They must all be numbers, so I use the string method
    isnumeric(). If that passes, I then convert the substring to an
    integer for the remaining tests. I check to see that the substring
    is within valid range. Then I ensure that there are no leading
    zeros on any zero values. Finally, I check for leading zeros on any
    other values.
    If all tests pass, the algorithm returns true.
    -------------------------------------------------------------------
    '''

    s = inputString.split(".")

    if len(s) != 4:
        return False

    for x in s:
        if not x.isnumeric():
            return False
        else:
            y = int(x)
            if 0 > y or 255 < y:
                return False
            if y == 0 and x != "0":
                return False
            if y != 0 and x[0] == "0":
                return False

    return True


import ipaddress
def creative(inputString):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    vanpet90 from Armenia has a cheeky solution to this problem. They
    imported ipaddress, which is an IP manipulation library in Python.
    The function ip_address(string) within the library allows one to
    create an IP object from a valid IP string. This will fail if the
    string does not conform to the same rules listed in the problem.
    So, vanpet90 uses a try-except clause that returns False if the
    object cannot be created, and true otherwise. Sneaky, sneaky!
    -------------------------------------------------------------------
    '''

    try:
        ipaddress.ip_address(inputString)        
    except:
        return False
    return True