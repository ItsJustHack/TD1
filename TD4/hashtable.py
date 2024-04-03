INITIAL_LENGTH = 10

class Hashtable:

    def __init__(self, hash_function):
        self.__hash_function = hash_function
        self.__length = INITIAL_LENGTH # Useful if we want to increase N
        self.__table = []
        for i in range(self.__length):
            self.__table.append([])

    def __str__(self):
        return str(self.__table)


    def put(self, key, value): 
        pos = self.__hash_function(key) % self.__length
        if (key, value) not in self.__table[pos]:
            self.__table[pos].append((key, value))
        else : 
            # truc immonde mais flemme de réfléchir
            i = [key for (key, value) in self.__table[pos]].index(key)
            self.__table[pos][i] = (key, value)



def first_hash_function(x : str):
    """ Create the first naïve hash function"""
    return sum([ord(char) for char in x])
