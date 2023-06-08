def longest_consecutive_sequence(nums: list):
    # sort list
    # check consecutive sequence, save in list
    nums.sort()
    count = 1
    for i, num in enumerate(nums):
        if num == nums[i-1] + 1:
            count += 1
    return count



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""