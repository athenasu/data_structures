
def group_anagrams(strings: list):
    # Goal: group the same anagrams together in lists
    # need to sort them into the same order in order to compare
    grouped_anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in grouped_anagrams:
            grouped_anagrams[sorted_string].append(string)
        else:
            grouped_anagrams[sorted_string] = [string]
    return list(grouped_anagrams.values())





print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""