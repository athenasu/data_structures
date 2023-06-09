def remove_duplicates(nums:list):
    """
        Given a sorted list of integers, 
        rearrange the list in-place such that all unique elements appear at the beginning of the list, 
        followed by the duplicate elements
        Return new length of list containing unique elements
        Steps:
            1. if empty list, return 0
            2. Create 2 indicies to compare two numbers
            3. If the same, one index increases. If not the same, increase the other index by 1 and swap values
        Note: 
            1. Should not create new list
            2. Should not use any additional data structures
            3. Original list should be modified in-place
    """

    # Other Solution: this does not keep the original values in the list
    if not nums:
        return 0
    
    nums.sort()
    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write

    # Solution 1: keeps all original items in list
    # if not nums:
    #     return 0
    
    # nums.sort()
    # writer, pointer = 0, 1
    # while pointer < len(nums):
    #     if nums[writer] == nums[pointer]:
    #         pointer += 1
    #     else:
    #         writer += 1
    #         nums[writer], nums[pointer] = nums[pointer], nums[writer]
    #         pointer += 1
    # return writer + 1
    

    
    

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])
print(nums)


"""
    EXPECTED OUTPUT:
    ----------------
    New length: 5
    Unique values in list: [0, 1, 2, 3, 4]

"""