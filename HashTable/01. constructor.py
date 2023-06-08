"""
    Build HashTable constructor and hash method
"""

class HashTable:
    def __init__(self, size = 7) -> None:
        # by default, this will create a map with 7 None items in it
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # ord(letter) is getting the ascii number for the letter in the key we pass in
            # * 23 because 23 is a prime number, we can put any prime number here
            # mod by 7, so the remainder will be anywhere from 0-7
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for index, value in enumerate(self.data_map):
            print(f'{index}: {value}')
    

my_ht = HashTable()

my_ht.print_table()