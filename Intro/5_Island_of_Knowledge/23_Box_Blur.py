import numpy # numpy is automatically imported in CodeSignal
def solution(image):
    '''
    EXPLANATION
    -------------------------------------------------------------------
    I utilize numpy for 2D indexing, otherwise the library is unused.
    A nested for loop is used to iterate over each pixel (excluding the
    border pixels), and then an even deeper nested for loop calculates
    the blurred value. Appending methods create the new array a that
    contains the blurred image.

    These nested for loops are not optimal in a general sense for
    programming, since it increases time complexity greatly. However,
    in the limited use given by the constraints, they are acceptable in
    this situation.

    There are more efficient approaches, particularly by only
    calculating the pixels that have changed within the window instead
    of the entire window every time (subtracting previous pixels / 9
    and adding new pixels / 9) but that creates a more complex
    algorithm, and I believe my answer suffices for the problem at hand
    -------------------------------------------------------------------
    '''

    image = numpy.array(image)
    a = [] # new image
    for i in range(1, len(image) - 1):
        temp = [] # one row
        for j in range(1, len(image[0]) - 1):
            temp2 = 0
            for x in image[i-1:i+2, j-1:j+2]:
                temp2 += sum(x)
            temp.append(temp2//9) # add value to row
        a.append(temp) # add row to image
    return a
