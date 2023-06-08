"""
    use a dictionary to find a key that is the same
    (common interview question)
"""

def item_in_common(list1, list2) -> bool:
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for key in list2:
        if key in my_dict:
            return True
    return False


list1 = [1, 2, 3]
list2 = [5, 4, 3]

print(item_in_common(list1, list2))