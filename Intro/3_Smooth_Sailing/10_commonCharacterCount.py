def solution(s1, s2):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    I approached this problem by creating two dictionaries, one for
    each string. These dictionaries are formatted with characters as
    keys, and counts as values. I then iterate over each string,
    counting the instances of each character.
    Finally, I iterate over the first dictionary, and if that character
    exists in the second dictionary, I add the lesser of the two values
    to create a total count of shared characters.
    -------------------------------------------------------------------
    '''
    
    s1_dict = {}
    s2_dict = {}
    count = 0
    for letter in s1:
        s1_dict[letter] = s1.count(letter)
        s1.replace(letter, "")
    for letter in s2:
        s2_dict[letter] = s2.count(letter)
        s2.replace(letter, "")
    for letter in s1_dict:
        if letter in s2_dict:
            if s1_dict[letter] > s2_dict[letter]:
                count += s2_dict[letter]
            else:
                count += s1_dict[letter]
    return count

def concise(s1, s2):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    keeping_it_leal from Germany comes back again with this far more
    concise solution to the problem utilizing Python's set() function.
    The set function returns all unique elements of an iterable. By
    using this, we can simply create an array of the minimum counts
    of each unique character in EITHER string (s1 chosen here), and
    return the sum of these counts. If the character doesn't exist in
    the second string, the minimum will therein be zero, which is a
    more implicit way to compare characters between the strings.
    -------------------------------------------------------------------
    '''

    return sum([min(s1.count(c),s2.count(c)) for c in set(s1)])
            
        
        
        
