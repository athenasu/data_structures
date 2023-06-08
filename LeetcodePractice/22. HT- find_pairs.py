def find_pairs(list1, list2, target):
    # return all the tuples with two integers that add up to the target
    result_set = set(list1)
    results = []
    for num in list2:
        difference = target - num
        if difference in result_set:
            results.append((difference, num))
    return results




list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(list1, list2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""