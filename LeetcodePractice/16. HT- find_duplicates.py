def find_duplicates(num_list: list):
    # create an empty hash table
    dictionary = {}
 
    # iterate through each number in the array
    for num in num_list:
        # add the number to the hash table or increment its count if it's already in the hash table
        dictionary[num] = dictionary.get(num, 0) + 1
 
    # create a list of the numbers that appear more than once in the input array
    results = [num for num, count in dictionary.items() if count > 1]
    # return the list of duplicates
    return results


    ##### solution 1 #####
    # # use a dictionary to check if there are duplicates
    # lookup_dict = {}
    # dupe_list = []
    # for num in num_list:
    # # lookup the number
    # # if it doesn't exist, add the numbers into the dictionary, set the value to be False
    #     if num in lookup_dict.keys():
    #         if num not in dupe_list:
    #             dupe_list.append(num)
    #     else:
    #         lookup_dict[num]=True
    # return dupe_list




print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

