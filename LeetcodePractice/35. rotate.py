from typing import List


def rotate(nums: List, k):
    """
        Takes the list of integers and an integer k as input and rotates the list to the right by k steps.
        Note: 
            1. nums[:] = whole list
            2. nums[-k:] = not including nums[k]
            3. nums[:-k] = including nums[k]
    """
    # check if k is bigger than the list
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""