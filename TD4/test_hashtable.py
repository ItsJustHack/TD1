import unittest 
from hashtable import Hashtable 
from hashtable import first_hash_function 

class TestHashtable(unittest.TestCase):
    def setUp(self):
        self.hash_test = Hashtable(first_hash_function)

    def test_create_hash(self):
        self.assertEqual(first_hash_function("abc"), 294)

    def test_put(self):
        self.hash_test.put("abc", 1)
        self.hash_test.put("ab", 2)
        self.hash_test.put("a", 3)
        self.hash_test.put("abcd", 4)
        self.hash_test.put("abce", 5)
        self.hash_test.put("abcef", 6)
        print(self.hash_test)
        
        

if __name__ == "__main__":
    unittest.main()
