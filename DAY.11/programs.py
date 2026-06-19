# tree data structure:
# #it it a non linear data structure in which a collection of elements known as node as connected to each other via edges
#  there exits exactly one path between any two nodes
#TRAVERSAL
#DFS:DEPTH SOR SEARCH
#BFS:BREADTH FOR SEARCH
#LEFT VIEW TRAVERSAL
#TREENODE: 
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,value):     

        