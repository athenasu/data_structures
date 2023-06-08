def find_max_min(nums:list):
    """
        Takes a list of integers as input
        Returns a tuple containing the maximum and minimum values in the list
    """
    max_val = min_val = nums[0]
    for item in nums:
        if item > max_val:
            max_val = item
        elif item < min_val:
            min_val = item
    return (max_val, min_val)
    


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""