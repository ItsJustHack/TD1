class Noeud:

    def __init__(self, label, *children):

        self.set_label(label)
        self.set_children(children)

    def label(self):
        return f"Label : {self.label}"

    def set_label(self, label):
        if not isinstance(label, str):
            raise "Label is not of type string"
        self.label = label

    def set_children(self, children):
        for child in children:
            if not isinstance(child, Noeud):
                raise "Child is not an instance of Noeud"

        self.children = children

    def fchildren(self):
        return self.children

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
        return len(self.children) == 0

    def depth(self):
        if self.is_leaf():
            return 0
        return 1 + max([child.depth() for child in self.children])

