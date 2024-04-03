INITIAL_LENGTH = 10

class Hashtable:

    def __init__(self, hash_function, length = INITIAL_LENGTH):
        self.__hash_function = hash_function
        self.__length = length # Useful if we want to increase N
        self.__table = self.create_table()


    @property
    def table(self):
        """The table property."""
        return self.__table
    @table.setter
    def table(self, value):
        self.__table = value

    @property
    def length(self):
        """The length property."""
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    def __str__(self):
        """Returns the table as a string"""
        return str(self.table)

    def keys_pos(self, pos):
        """Returns the keys at position pos"""
        return [key for (key, value) in self.__table[pos]]

    def values_pos(self, pos):
        """Returns the values at position pos"""
        return [key for (key, value) in self.__table[pos]]

    def nb_elements(self):
        """ Returns the number of tuple (key, value) in the table"""
        return sum([len(position) for position in self.table])

    def put(self, key, value): 
        """Add a value to the hashing table"""
        pos = self.__hash_function(key) % self.length
        if (key, value) not in self.table[pos]:
            self.table[pos].append((key, value))
        else : 
            i = self.keys_pos(pos).index(key)
            self.table[pos][i] = (key, value)
    
    def put_auto_resize(self, key, value): 
        """Add a value to the hashing table"""
        pos = self.__hash_function(key) % self.length
        if self.nb_elements() >= 10*self.length:
            print("The table have been resized", self.length)
            self.resize()
        if (key, value) not in self.table[pos]:
            self.table[pos].append((key, value))
        else : 
            i = self.keys_pos(pos).index(key)
            self.table[pos][i] = (key, value)

    def get(self, key):
        """Get a value from a key"""
        pos = self.__hash_function(key) % self.length
        keys = self.keys_pos(pos) 
        if key not in keys: 
            return None
        else:
            return self.table[pos][keys.index(key)][1]

    def repartition(self):
        """Print the repartition of collisions"""
        import matplotlib.pyplot as plt
        y = [len(self.keys_pos(pos)) for pos in range(self.length)]
        x = range(self.length)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()

    def create_table(self):
        table = []
        for i in range(self.__length):
            table.append([])
        return table

    def resize(self):
        self.length *= 2
        new_hashtable = Hashtable(self.__hash_function, self.length)
        for position in self.table:
            for (key, value) in position:
                new_hashtable.put(key, value)
        self.table = new_hashtable.table
        



def first_hash_function(x : str):
    """ Create the first naïve hash function"""
    return sum([ord(char) for char in x])


def second_hash_function(x : str): 
    """ Create a better hash function"""
    h = 0
    for (i, char) in enumerate(x):
        h = 31*h + ord(char)
    return h
