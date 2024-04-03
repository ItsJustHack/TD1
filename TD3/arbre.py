class Noeud:

    def __init__(self, label, *children):

        self.set_label(label)
        self.set_children(children)

    def __str__(self):
        if self.is_leaf():
            return self.label()
        string = self.label() + '('
        for child in self.children():
            string += child.__str__() + ','
        string = string.rstrip(',') + ")"
        return string

    def __eq__(self, other):
        if not isinstance(other, Noeud):
            return False
        if self.label() != other.label():
            return False
        if len(self.children()) != len(other.children()):
            return False
        for self_child, other_child in zip(self.children(), other.children()):
            if self_child != other_child:
                return False
        return True

    def label(self):
        return f"{self.__label}"

    def set_label(self, label):
        if not isinstance(label, str):
            raise "Label is not of type string"
        self.__label = label

    def set_children(self, children):
        for child in children:
            if not isinstance(child, Noeud):
                raise "Child is not an instance of Noeud"
        self.__children = children

    def children(self):
        return self.__children

    def nb_children(self):
        if self.is_leaf():
            return 0
        return len(self.__children) + sum([child.nb_children() for child in
                                         self.children()])

    def child(self, i: int):
        if i >= self.nb_children() or i < 0:
            raise "Index out of bounds, not enough children"
        return self.__children[i]

    def is_leaf(self):
        return len(self.__children) == 0

    def depth(self):
        if self.is_leaf():
            return 0
        return 1 + max([child.depth() for child in self.__children])

    def deriv(self, var: str) -> 'Noeud':
        if self.is_leaf():
            if self.label() == var:
                return Noeud('1')
            else:
                return Noeud('0')
        else:
            if self.label() == '+':
                return Noeud('+', *[child.deriv(var) for child in self.children()])
            elif self.label() == '*':
                if any(child.label() == var for child in self.children()):
                    # The fun part 
                    L = []
                    T = []
                    i = 0
                    for child in self.children():
                        for j in range(len(self.children())):
                            if j == i:
                                T.append(self.child(i).deriv(var))
                            else:
                                T.append(self.child(i))
                        L.append(Noeud('*', *T))
                        T = []
                        i+=1
                    print(L)
                    return Noeud('+', *L)
                else:
                    return Noeud('0')
            else:
                raise ValueError("Unsupported operator")

