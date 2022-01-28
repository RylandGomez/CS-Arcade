def oneline(inputArray):

    return max([inputArray[i]*inputArray[i+1] for i in range(len(inputArray) - 1)])

def expanded(inputArray):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    The previous solution uses a list comprehension that accomplishes
    the same as below. Comments are added to explain the process.
    List comprehensions are generally computationally cheaper, as they
    always utilize Python's list.append() function. However, they can
    quickly become hard to read. This algorithm is a simple one, and
    it already showcases that difference, which only increases as
    complexity increases.
    -------------------------------------------------------------------
    '''

    products = []
    
    # only iterate to second to last value, since it will be the last pair
    for i in range(0, len(inputArray) - 1):
        x = i # first index in pair
        y = i + 1 # second index in pair
        z = inputArray[x] * inputArray[y] # product of pair
        products.append(z) # add product to output list
    
    return max(products) # return largest product found from list
