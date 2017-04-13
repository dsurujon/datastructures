class ArrayTree():
        def __init__(self,index,data,children=None,level=0):
                children=[]
                if children is not None:
                        for child in children:
                                self.add_child(child)
                self.tree=[[index,data,children,level]]
        def make_node(data,index,children=None,level=0):
                return ArrayTree(data, index,children,level).tree[0]
        def get_node(self,node):
                return self.tree[node]
        def add_child(self,node,child):
                #update the level of the child
                child[3]=self.tree[node][3]+1
                #add the child's index to the children of the parent
                self.tree[node][2].append(child[0])
                self.tree.append(child)
                
        def print_tree(self,node=0,indexing=False):
                #print data unless indexing is specified
                index_to_print=1
                #in which case print the tree index of the nodes
                if indexing: index_to_print=0
                current_node=self.tree[node]
                nodestr=current_node[3]*" "+str(current_node[1])
                print(nodestr)
                if current_node[2]!=[]:
                        for childnode in current_node[2]:
                                self.print_tree(node=childnode)
                else:
                        pass
