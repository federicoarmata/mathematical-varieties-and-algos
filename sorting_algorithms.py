################################################
## Problem:
## Write 3 sorting algorithms to sort n distinct 
## values A_1, A_2, ..., A_n and analyse the 
## complexity of each algo.
#################################################


### Insertion sort: O(n^2)
def insertion_sort(input_list):
    """
    Sort input array by using the insertion sort algorithm.

    Parameters:
    ----------
    input_list: input_array, list.

    Output:
    ------
    return the sorted array.
    """   
    for i in range(len(input_list)):
        for j in range(i-1, 0, -1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
            else:
                break
                
    return input_list


### Merge sort: O(n*log(n))
def split(input_list):
    """
    Splits a list into two pieces.

    Parameters:
    ----------
    input_list: list

    Output:
    ------
    return: left and right lists, (list, list)
    """

    input_list_len = len(input_list)
    midpoint = input_list_len // 2

    return input_list[:midpoint], input_list[midpoint:]


def merge_sorted_lists(list_left, list_right):
    """
    Merge two sorted lists.
    Linear operation:
    O(len(list_right) + len(list_right))
    
    Parameters:
    ----------
    left_list: list
    right_list: list

    Output:
    ------
    return: merged list
    """

    # Special case: if one or both of lists are empty
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left

    print(list_left, list_right)
    
    # General case
    index_left = index_right = 0
    list_merged = []
    list_len_target = len(list_left) + len(list_right)
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            # Value on the left list is smaller (or equal so it should be selected)
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            list_merged.append(list_right[index_right])
            index_right += 1
            
        # If at the end of one of the lists, take this shortcut
        if index_right == len(list_right):
            # Reached the end of right
            # Append the remainder of left and break
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            # Reached the end of left
            # Append the remainder of right and break
            print(index_right)
            print(list_right[index_right:])
            list_merged += list_right[index_right:]
            print(list_merged)
            break
        
    return list_merged

def merge_sort(input_list):
    """
    Sort input array by using the merge sort algorithm.

    Parameters:
    ----------
    input_list: input_array, list.

    Output:
    ------
    return the sorted array.
    """

    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        # most important line of the algo;
        return merge_sorted_lists(merge_sort(left), merge_sort(right))  


### Quicksort: O(n*log(n))
def quick_sort(input_array):
    """
    Sort input array by using the quick sort algorithm.

    Parameters:
    ----------
    input_list: input_array, list.

    Output:
    ------
    return the sorted array.
    """

    smaller = []
    larger = []
    equal = []

    if len(input_array) > 1:
        pivot = input_array[0]
        for x in input_array:
            if x < pivot:
                smaller.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                larger.append(x)
        return quick_sort(smaller) + equal + quick_sort(larger)
    else:  
        # handle the part at the end of the recursion: when 
        # you only have one element in your array, just 
        # return the array.
        return input_array



