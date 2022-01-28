def solution(a):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    I made the problem as explicit for myself as possible. I created a
    list of the people in the array by excluding the -1 values, then
    sorted them. They will be added in that order later.
    Then, I created a boolean array of the tree locations. This is the
    same length as the original array, since we are not adding or
    removing people.
    Finally, I append either -1 (for trees) or the next person to the
    initially empty answer list, and return it. I utilize the pop()
    method to continually use the 0 index.
    -------------------------------------------------------------------
    '''

    people = [x for x in a if x != -1]
    people.sort()
    trees = [True if x == -1 else False for x in a]
    
    answer = []
    for boolean in trees:
        if boolean == True:
            answer.append(-1)
        else:
            answer.append(people.pop(0))
    return answer


def alternative(a):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    An alternate approach was made by andrew_pudge from the US. This
    approach still creates a sorted list of the people. However,
    instead of creating a brand new array, we simply identify the
    indices of the trees and inserts the -1 values into the created
    "people" array.
    -------------------------------------------------------------------
    '''

    arr = sorted([x for x in a if x != -1])
    for i, x in enumerate(a):
        if x == -1:
            arr.insert(i, -1)
    return arr

def condense(a):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    edson_m3 from Brazil utilized list comprehension to perform my
    initial solution in a concise manner. The format is given below.
    Note the use of filter and lambda. Perhaps comparing this use to
    my initial solution can help understand their use. The first line
    accomplishes the same as a list comprehension of
    sorted([x for x in a if x != -1]). Also note the syntax of the
    if-else list comprehension in the return line, which is a useful
    syntax to learn if you're not aware of it.
    -------------------------------------------------------------------
    '''
    
    people = sorted(filter(lambda x: x != -1, a))
    return [people.pop(0) if i != -1 else -1 for i in a]