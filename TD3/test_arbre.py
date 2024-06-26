import unittest
from arbre import Noeud

class TestTreeMethods(unittest.TestCase):

    def setUp(self):
        self.n1 = Noeud('4')
        self.n2 = Noeud('2', self.n1)
        self.n3 = Noeud('1', Noeud('2', Noeud('3', Noeud('4'))))
        self.n4 = Noeud('1', Noeud('2', Noeud('3', Noeud('4'), Noeud('5'))))
        self.polynome = Noeud('*', Noeud('X'), Noeud('X'))

    def test_is_leaf(self):
        self.assertTrue(Noeud('4').is_leaf())
        self.assertFalse(Noeud('1', Noeud('2')).is_leaf())

    def test_nb_children(self):
        self.assertEqual(self.n2.nb_children(), 1)
        self.assertEqual(self.n1.nb_children(), 0)
        self.assertEqual(self.n3.nb_children(), 3)

    def test_children(self):
        self.assertEqual(self.n2.children()[0], self.n1)

    def test_depth(self):
        self.assertEqual(self.n2.depth(), 1)
        self.assertEqual(self.n1.depth(), 0)
        self.assertEqual(self.n3.depth(), 3)

    def test_str(self):
        print("Affichage du noeud", self.n1)
        print("Affichage du noeud", self.n2)
        print("Affichage du noeud", self.n3)
        print("Affichage du noeud", self.n4)
        print(self.polynome.deriv('X'))
        


if __name__ == '__main__':
    unittest.main()



