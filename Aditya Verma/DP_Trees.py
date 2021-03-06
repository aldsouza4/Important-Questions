# implementation for binary search tree

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)

        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        # checking the left Subtree
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)

        # checking the right Subtree
        if data > node.data:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)

    def getmin(self):
        if self.root is None:
            return
        node = self.root
        while node.left:
            node = node.left
        return node.data

    def getmax(self):
        if self.root is None:
            return
        node = self.root
        while node.right:
            node = node.right
        return node.data

    def traverse(self):
        if self.root is not None:
            return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)

        print(node.data)

        if node.right:
            self.traverse_in_order(node.right)

    def get_max(self):
        if self.root:
            return self.get_max_node(self.root)

    def get_max_node(self, node):
        if node.right:
            return self.get_max_node(node.right)
        else:
            return node.data

    def get_min(self):
        if self.root:
            return self.get_min_node(self.root)

    def get_min_node(self, node):
        if node.left:
            return self.get_min_node(node.left)
        else:
            return node.data

    def remove(self, data):
        if self.root is not None:
            return self.remove_Node(data, self.root)

    def remove_Node(self, data, node):

        if node is None:
            return

        if data > node.data:
            self.remove_Node(data, node.rightChild)
        elif data < node.data:
            self.remove_Node(data, node.leftChild)
        else:
            if node.leftChild is None and node.rightChild is None:
                print("Removing a leaf Node")

                parent = node.parent

                if parent is not None and parent.right == node:
                    parent.right = None
                if parent is not None and parent.left == node:
                    parent.left = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rightChild is not None:
                print("Removing a node with a single right child")

                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.rightChild
                    if parent.right == node:
                        parent.right = node.rightChild

                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent

                del node

            elif node.rightChild is None and node.leftChild is not None:
                print("Removing a node with a single left child")

                parent = node.parent

                if parent is not None:
                    if parent.right == node:
                        parent.right = node.rightChild
                    if parent.left == node:
                        parent.left = node.rightChild
                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print("Removing a node with two children ")

                predesr = self.get_predessor(node.leftChild)

                temp = predesr.data
                predesr.data = node.data
                node.data = temp

                self.remove_Node(data, predesr)

    def get_predessor(self, node):
        if node.right:
            return self.get_predessor(node.right)

        return node

    # Diameter of Tree Given a binary tree, you need to compute the length of the diameter of the tree.
    # The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    # This path may or may not pass through the root.

    def diameter(self):
        self.result = 0

        def get_diameter(node: Node):
            if node is None:
                return 0

            res_l = get_diameter(node.left)
            res_r = get_diameter(node.right)

            temp = 1 + max(res_l, res_r)
            ans = max(temp, 1 + res_l + res_r)
            self.result = max(ans, self.result)

            return temp

        get_diameter(self.root)
        return self.result

    # For this problem, a path is defined as any sequence of nodes from some starting node to
    # any node in the tree along the parent-child connections. The path must contain at least one
    # node and does not need to go through the root.

    def max_sum_path(self):
        self.result = -float('inf')

        def maxpath(node: Node):
            if node is None:
                return 0

            left = maxpath(node.left)
            right = maxpath(node.right)

            temp = max(max(left, right) + node.data, node.data)
            ans = max(left + right + node.data, temp)
            self.result = max(ans, self.result)
            return temp

        maxpath(self.root)
        return self.result

    # For this problem, a path is defined as any sequence of nodes from some starting leaf node to
    # any leaf node in the tree along the parent-child connections. The path must contain at least one
    # node and does not need to go through the root.

    def max_sum_path_leaf(self):
        self.result = -float('inf')

        # This is Wrong
        def maxpath_leaf(node: Node):
            if node is None:
                return 0

            left = maxpath_leaf(node.left)
            right = maxpath_leaf(node.right)

            temp = max(left, right) + node.data
            ans = max(temp, left + right + node.data)
            self.result = max(self.result, ans)

        maxpath_leaf(self.root)
        return self.result


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    bst.insert(28)
    print(bst.max_sum_path_leaf())
