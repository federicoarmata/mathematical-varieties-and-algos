######################################################
## Problem:
## Given a sorted array, write a func to extract the 
## unique elements. 
## Example: [1, 1, 3, 3, 3, 5, 5, 5, 9, 9, 9, 9],
## should return [1, 3, 5, 9].
######################################################

def extract_unique_elements(sorted_array):
    """
    Parameters:
    ----------
    sorted_array:
        list object, sorted.
        
    Output:
    ------
    array_extracted:
        list object, with extracted unique elements
    """

    array_extracted = []
    array_extracted.append(sorted_array[0])

    for i in range(len(sorted_array)-1):

        if sorted_array[i+1] is not sorted_array[i]:
            array_extracted.append(sorted_array[i+1])
    
    return array_extracted


extract_unique_elements([1, 1, 3, 3, 3, 5, 5, 5, 9, 9, 9, 9])