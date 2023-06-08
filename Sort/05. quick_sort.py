"""
    quick sort function
"""

def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    """
        Sort items into two separate sections, one less than the pivot value, the other greater than the pivot value
        Steps:
            1. Pivot value = first item in list
            2. Traverse through list and compare item to pivot value
            3. If greater than, stays in place
            4. If less than, swaps with first greater than value
            5. After traversing through the list, switch pivot value with last less than value
            6. Return pivot index
    """
    swap_index = pivot_index # swap_index = 0 ## swap_index = 4 ([6, 7, 5])
    for i in range(pivot_index + 1, end_index + 1): ## 5, 6 (5, 7)
        if my_list[i] < my_list[pivot_index]: # if 1 < 2: # if 6 7 < 6, ; ## if 5 < 7
            swap_index += 1 # swap_index = 1 ## swap_index = 5
            swap(my_list, i, swap_index) # swapping item 0 and item 1 ## swap item 6, 5 ([6, 5, 7])
    swap(my_list, swap_index, pivot_index) # swap(my_list, 1, 1) ## swap(my_list, 5, 4) -> ([5, 6, 7])
    return swap_index # return 1 ## return 5

def quick_sort_helper(my_list, left, right): # my_list, 0, 6 ## my_list, 0, 2 ### my_list, 0, 1 ## my_list, 4, 6
    """
        Recursively sort the list on the right and left side of the pivot value
    """
    if left < right: # 0 < 6 ## 0 < 2
        pivot_index = pivot(my_list, left, right) # 3 ([2, 1, 3, 4, 6, 7, 5]) ## 1 ([1, 2, 3]) ## 5 ([5, 6, 7]) 
        quick_sort_helper(my_list, left, pivot_index - 1) # my_list, 0, 2 ([2, 1, 3]) ## my_list, 0, 0 (exits)
        quick_sort_helper(my_list, pivot_index + 1, right) # my_list, 4, 6 ([6, 7, 5]) ## my_list, 6, 6 (exits)

    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

unsorted_list = [4, 6, 1, 7, 3, 2, 5]

print(quick_sort(unsorted_list))