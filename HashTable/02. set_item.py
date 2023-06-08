"""
    Build set_item method
"""

class HashTable:
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        # need to check if a spot in the address or index is free (in this case, "None")
        if self.data_map[index] == None:
            # if it is None, so nothing is stored there, we will initiate the outer list
            self.data_map[index] = []
        # add the item into the list
        self.data_map[index].append([key, value])

    def print_table(self):
        for index, value in enumerate(self.data_map):
            print(f'{index}: {value}')
    

my_ht = HashTable()

my_ht.set_item('bolts', 1400)
my_ht.set_item('washers', 50)
my_ht.set_item('lumber', 70)

my_ht.print_table()