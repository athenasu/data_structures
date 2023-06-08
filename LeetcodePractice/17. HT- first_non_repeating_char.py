
def first_non_repeating_char(string: str):
    # two for loops
    dictionary = {}
    # 1 go through the words and add them to the dict
    for char in string:
        dictionary[char] = dictionary.get(char, 0) + 1
    # 2 check from beginning if the value is only 1, if so, return
    # for letter in string:
    #     if dictionary.get(letter) == 1:
    #         return letter
    ## OR ##
    for letter, count in dictionary.items():
        if count == 1:
            return letter
    # else return None
    return None



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""