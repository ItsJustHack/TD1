import unittest 
from hashtable import Hashtable 
from hashtable import first_hash_function 
from hashtable import second_hash_function 

class TestHashtable(unittest.TestCase):
    def setUp(self):
        self.hash_test = Hashtable(first_hash_function)
        self.hash_test.put("abc", 1)
        self.hash_test.put("ab", 2)
        self.hash_test.put("a", 3)
        self.hash_test.put("abcd", 4)
        self.hash_test.put("abcde", 5)
        self.hash_test.put("abcdef", 6)

    def test_create_hash(self):
        self.assertEqual(first_hash_function("abc"), 294)

    def test_get(self):
        self.assertEqual(self.hash_test.get("abc"), 1)
        self.assertEqual(self.hash_test.get("b"), None)
        self.assertEqual(self.hash_test.get("ab"), 2)
        self.assertEqual(self.hash_test.get("a"), 3)
        self.assertEqual(self.hash_test.get("abcd"), 4)
        self.assertEqual(self.hash_test.get("abcde"), 5)
        self.assertEqual(self.hash_test.get("abcdef"), 6)

    def test_repartition(self):
        self.hash_test.repartition()

    def test_french_dictionnaire_first_hash(self):
        try:
            h = Hashtable(first_hash_function, 320)
            f = open("frenchssaccent.dic")
            for ligne in f:
                mot = ligne.rstrip("\n")
                h.put(mot, len(mot))
            h.repartition()
        except Exception as e:
            raise e

    def test_french_dictionnaire_second_hash(self):
        try:
            h = Hashtable(second_hash_function, 320)
            f = open("frenchssaccent.dic")
            for ligne in f:
                mot = ligne.rstrip("\n")
                h.put(mot, len(mot))
            h.repartition()
        except Exception as e:
            raise e

    def test_put_auto_resize(self):
        try:
            h = Hashtable(second_hash_function, 20)
            f = open("frenchssaccent.dic")
            for ligne in f:
                mot = ligne.rstrip("\n")
                h.put_auto_resize(mot, len(mot))
            h.repartition()
        except Exception as e:
            raise e


        

if __name__ == "__main__":
    unittest.main()
