class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class YourSolution(object):

    def inorderTraversal(self, root):
        array = []
        array = self.inorderTraversalInternal(root, array)
        return array

    def inorderTraversalInternal(self, root, array):
        if root.left is not None:
            self.inorderTraversalInternal(root.left, array)
        array.append(root.val)
        if root.right is not None:
            self.inorderTraversalInternal(root.right, array)
        return array


    def preorderTraversal(self, root):
        array = []
        array = self.preorderTraversalInternal(root, array)
        return array

    def preorderTraversalInternal(self, root, array):
        array.append(root.val)
        if root.left is not None:
            self.preorderTraversalInternal(root.left, array)
        if root.right is not None:
            self.preorderTraversalInternal(root.right, array)
        return array



if __name__ == '__main__':
    YS = YourSolution()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.left.left.left = TreeNode(4)
    tree.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    r = YS.preorderTraversal(tree)
    print("Pre-Order Traversal")
    for i in r:
        print(i)
    print("In-Order Traversal")
    r = YS.inorderTraversal(tree)
    for i in r:
        print(i)