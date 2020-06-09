from binarytree import bst, tree, heap, build
from BFS_Traversal import bfs_traverse
#my_bst = bst(height=5, is_perfect=False)
#print(my_bst)

# Ελενα κοιτα το δεντρο που φτιαξαμε εχει για παιδια οτι να ναι . Φτιαξε ενα
# δεντρο που να μην δεχεται παιδια στον constructor ( και να ειναι None και τα δυο ) .
# το value  να ειναι int . και θα εχει μια μεθοδο add_child(self,value). αν το value
# ειναι μεγαλυτερο απο το self.value του τοτε αν εχει δεξι παιδι θα του λεει καντο εσυ add.
# Αν δεν εχει δεξι παιδι θα δημιουργει ενα νεο node με αυτο το value και θα το κανι δεξι
# παιδι του. Αντιστοιχα για την αριστερη πλευρα

class MyBstNode:

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, value):
        if value > self.value:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = MyBstNode(value)
        elif value < self.value:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = MyBstNode(value)


    def print_Tree(self):
        if self.left:
            self.left.print_Tree()
        print(self.value)
        if self.right:
            self.right.print_Tree()



root = MyBstNode(10)
root.add_child(1)
# root.add_child(11)
print(build(bfs_traverse(root)))
lst = [1, 23, 5, 45, 2, 6, 78, 64]
for x in lst:
    # print(build(bfs_traverse(root)))
    # dummy = input("Print Next:")
    root.add_child(x)
# print(build(bfs_traverse(root)))
root.print_Tree()

