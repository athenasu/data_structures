"""
    merge sort function
"""

def merge_sort(my_list):
    """
        Split list in half until every list only has one item, then sort and combine
        Steps:
            1. Split lists in half until every list only has one item, then call the helper to merge
                a. recursive function
                b. find the mid index of the list
                c. break down into two lists recursively until there is only 1 item left
                d. then merge items
            2. create a helper function for merging two lists
                a. while there are still items in both lists, compare items and add smallest to new list
                b. after both lists are empty, run another while loop to add the remainder of the list
    """
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

def merge(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list1):
        combined.append(list2[j])
        j += 1
    
    return combined
    

unsorted_list = [1, 2, 7, 8, 3, 4, 5, 6]

sorted_list = merge_sort(unsorted_list)

print(f'Unsorted list: {unsorted_list}')
print(f'Sorted list: {sorted_list}')

# my_list1 = [1, 4]
# my_list2 = [2, 3]
# print(merge(my_list1, my_list2))