from typing import List


def rotate(nums: List, k):
    """
        Takes the list of integers and an integer k as input and rotates the list to the right by k steps.
    
    """
    # Solution 2
    # checking to see if k == len(nums) or k > len(nums)
    
    # nums[:] = whole list, nums[-k:] = not including nums[k], nums[:-k] = including nums[k]
    pass
    

    


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""

# Solution 1
# for _ in range(k):
#     nums.insert(0, nums.pop())

# Solution 2
# k = k % len(nums)
# nums[:] = nums[-k:] + nums[:-k]