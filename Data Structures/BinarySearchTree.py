# implementation for binary search tree

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.rightChild = None
        self.leftChild = None


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
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)

        # checking the right Subtree
        if data > node.data:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

    def getmin(self):
        if self.root is None:
            return
        node = self.root
        while node.leftChild:
            node = node.leftChild
        return node.data

    def getmax(self):
        if self.root is None:
            return
        node = self.root
        while node.rightChild:
            node = node.rightChild
        return node.data

    def traverse(self):
        if self.root is not None:
            return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def get_max(self):
        if self.root:
            return self.get_max_node(self.root)

    def get_max_node(self, node):
        if node.rightChild:
            return self.get_max_node(node.rightChild)
        else:
            return node.data

    def get_min(self):
        if self.root:
            return self.get_min_node(self.root)

    def get_min_node(self, node):
        if node.leftChild:
            return self.get_min_node(node.leftChild)
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
            # case 1
            if node.leftChild is None and node.rightChild is None:
                print("Removing a leaf Node")

                parent = node.parent

                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None
                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None

                if parent is None:
                    self.root = None

                del node

            # case 2
            elif node.leftChild is None and node.rightChild is not None:
                print("Removing a node with a single right child")

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild

                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent

                del node

            # case 3
            elif node.rightChild is None and node.leftChild is not None:
                print("Removing a node with a single left child")

                parent = node.parent

                if parent is not None:
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            # case 4
            else:
                print("Removing a node with two children ")

                predesr = self.get_predessor(node.leftChild)

                temp = predesr.data
                predesr.data = node.data
                node.data = temp

                self.remove_Node(data, predesr)

    def get_predessor(self, node):
        if node.rightChild:
            return self.get_predessor(node.rightChild)

        return node


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    bst.insert(28)
    bst.insert(5)
    bst.insert(20)
    bst.remove(10)
    bst.traverse()
    # bst.traverse()
    # print(bst.get_min())
    # print(bst.getmin())
    # print(bst.getmax())
