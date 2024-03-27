class Noeud:

    def __init__(self, label, *children):

        self.set_label(label)
        self.set_children(children)

    # Je pense que c'est pour des arbres binaires sinon je ne comprends 
    # comment faire pour les parenthèses :(
        
    def __str__(self):
        if self.is_leaf():
            return str(self.label())
        else:
            return f"{self.label()}({','.join(map(str, self.children()))})"

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
        return f"{self.label}"

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
        return len(self.children) + sum([child.nb_children() for child in
                                         self.children])

    def child(self, i:int):
        if  i >= self.nb_children() or i < 0:
            raise "Index out of bounds, not enough children"
        return self.children[i]

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
                    return Noeud('+', *[Noeud('*', *self.children()).deriv(var)])
                else:
                    return Noeud('0')
            else:
                raise ValueError("Unsupported operator")
        

