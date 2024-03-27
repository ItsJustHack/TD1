# -*- coding: utf-8 -*-

import unittest
from arbre import Noeud


class TestTree(unittest.TestCase):

    def test_create_tree1(self):
        a = Noeud('a')
        a1 = Noeud('a1', a)
        a2 = Noeud('a1', a, a)
        self.assertIsNotNone(a)
        self.assertIsNot(a, a1)
        self.assertIsNot(a1, a2)

    def test_create_tree2(self):
        a = Noeud('a')
        b = Noeud('b')
        fab = Noeud('f', a, b)
        ga = Noeud('g', a)
        gb = Noeud('g', b)

        self.assertEqual(a.label(), 'a')
        self.assertEqual(len(a.children()), 0)
        self.assertEqual(b.label(), 'b')
        self.assertEqual(len(b.children()), 0)

        self.assertEqual(fab.label(), 'f')
        self.assertEqual(fab.child(0), a)
        self.assertEqual(fab.child(1), b)

    def test_leaf(self):
        a = Noeud('a')
        ga = Noeud('g', a)

        self.assertTrue(a.is_leaf())
        self.assertFalse(ga.is_leaf())

    def test_depth(self):
        a = Noeud('a')
        b = Noeud('b')
        fab = Noeud('f', a, b)
        ga = Noeud('g', a)
        gb = Noeud('g', b)
        fagb = Noeud('f', a, gb)

        self.assertEqual(a.depth(), 0)
        self.assertEqual(fab.depth(), 1)
        self.assertEqual(ga.depth(), 1)
        self.assertEqual(gb.depth(), 1)
        self.assertEqual(fagb.depth(), 2)

    def test_eq_tree(self):
        a1 = Noeud('a')
        a2 = Noeud('a')
        fab1 = Noeud('f', Noeud('a'), Noeud('b'))
        fab2 = Noeud('f', Noeud('a'), Noeud('b'))

        self.assertEqual(a1, a2)
        self.assertEqual(fab1, fab2)
        
    def test_deriv_constant(self):
        X = Noeud('X')
        a = Noeud('a')
        zero = Noeud('0')
        self.assertEqual(a.deriv('X'), zero)
        self.assertEqual(zero.deriv('X'), zero)

    def test_deriv_X(self):
        X = Noeud('X')
        Y = Noeud('Y')
        zero = Noeud('0')
        un = Noeud('1')

        self.assertEqual(X.deriv('X'), un)
        self.assertEqual(Y.deriv('X'), zero)

    def test_deriv_addition(self):
        X = Noeud('X')
        zero = Noeud('0')
        un = Noeud('1')

        self.assertEqual(Noeud('+', X, X).deriv('X'), Noeud('+', un, un))
        self.assertEqual(Noeud('+', X, un).deriv('X'), Noeud('+', un, zero))

if __name__ == '__main__':
    unittest.main()
