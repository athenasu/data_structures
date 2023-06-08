def has_unique_chars(string: str):
    # Write a function called has_unique_chars that takes a string as input
    # returns True if all the characters in the string are unique, and False otherwise.

    no_dupes = len(set(string))
    if no_dupes == len(string):
        return True
    return False



print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""