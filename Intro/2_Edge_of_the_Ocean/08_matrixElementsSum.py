def solution(matrix):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    My approach was simple enough. Iterate over each value using row
    and column indices. If the value was 0, the room is haunted, thus
    that room and all remaining rooms in the column were haunted and
    ignored. I appended that column value into bad_cols and checked
    each column iteration to ensure that value didn't exist in a "bad"
    column. If everything checked out, I'd add the value of the room to
    the running total of total_sum.
    -------------------------------------------------------------------
    '''
    
    bad_cols = []
    total_sum = 0
    r = len(matrix) # row count
    c = len(matrix[0]) # column count

    for row in range(r):
        for column in range(c):
            if column in bad_cols: # column haunted previously
                continue # go to next column
            room = matrix[row][column]
            if room == 0: # haunted room
                bad_cols.append(column) # log bad column
            else:
                total_sum += room # good room, add to total
    return total_sum

def better(matrix):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    A solution I preferred was implemented by user keeping_it_leal from
    Germany. They chose to iterate over columns first, and then rows.
    This allows the nested loop to immediately break once a haunted
    room has been detected, removing the need for a bad_cols array, and
    thus speeding up the process.
    -------------------------------------------------------------------
    '''
    
    total_sum = 0
    r = len(matrix) # row count
    c = len(matrix[0]) # column count

    for column in range(c):
        for row in range(r):
            room = matrix[row][column]
            if room != 0: # valid room
                total_sum += room
            else: # all following rooms haunted including current
                break # check next column
    return total_sum
    