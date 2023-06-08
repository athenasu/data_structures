"""
    Build get_item method
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
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            # for loop is for the items in the big list
            for i in range(len(self.data_map[index])):
                # matching the first item [0], which is the stored key
                if self.data_map[index][i][0] == key:
                    # returning the value [1]
                    return self.data_map[index][i][1]
        return None

    def print_table(self):
        for index, value in enumerate(self.data_map):
            print(f'{index}: {value}')
    

my_ht = HashTable()

my_ht.set_item('bolts', 1400)
my_ht.set_item('washers', 50)
# my_ht.set_item('lumber', 70)

print(my_ht.get_item('bolts'))
print(my_ht.get_item('washers'))
print(my_ht.get_item('lumber'))

my_ht.print_table()