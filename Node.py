class Node(object):
    "Generic tree node."
    def __init__(self, data, index, level=0, parent=None, children=None):
        self.data = data
        self.index = index
        self.parent = parent
        self.level = level
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def add_child(self, node):
        self.children.append(node)
        node.parent=self
        node.level=self.level+1
    def is_leaf(self):
        return self.children==[]
    def print_node(self):
        indent=self.level*" "
        #if data==False:
        #    nodestr=str(self.index)
        #else:
        nodestr=str(self.data)
        chil=[i.data for i in self.children]
        print(indent+nodestr,chil)
    def print_tree(self):
        current_level=self.level
        current_node=self
        if current_node.is_leaf()==False:
            current_node.print_node()
            for childnode in current_node.children:
                childnode.print_tree()
        else:
            current_node.print_node()


