import random as r


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value and self.height == other.height

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, node, value):
        """
        Takes a value and inserts it into the tree in the form of a node
        :param node: the root/subroot of a tree for node to be added
        :param value: the value to be inserted
        :return: new root of tree
        """
        the_node = Node(value)

        if self.root is None:
            self.root = the_node
            #self.root.height += 1
            self.size += 1
        else:
            if node is None:
                node = the_node
                self.size += 1
            elif node.value > value:
                if node.left is None:
                    node.left = the_node
                    node.left.parent = node
                    self.size += 1
                else:
                    node.left = self.insert(node.left, value)
            elif node.value < value:
                if node.right is None:
                    node.right = the_node
                    node.right.parent = node
                    self.size += 1
                else:
                    node.right = self.insert(node.right, value)

            node.height = 1 + max(self.height(node.left), self.height(node.right))

        new_node = self.rebalance(node)

        return new_node

    def remove(self, node, value):
        """
        Removes a specific value from the tree
        :param node: root/subroot of tree to look for value and remove it
        :param value: Value to be removed from tree
        :return: new root of tree
        """
        if node is None:
            return
        elif value < node.value:
            return self.remove(node.left, value)
        elif value > node.value:
            return self.remove(node.right, value)
        else:
            if self.root.value == value and self.root.left is None and self.root.right is None:
                self.size -= 1
                original = self.root
                self.root = None
                self.root.parent = original.parent

            elif node.left is None and node.right is None:
                self.size -= 1

                the_parent = node.parent
                if node.parent.right is node:
                    node.parent.right = None
                    node = None
                else:
                    node.parent.left = None
                    node = None
                the_parent.height = 1 + max(self.height(the_parent.left), self.height(the_parent.right))
                self.rebalance(the_parent)

            elif node.left is None:
                self.size -= 1
                if self.root.value == node.value:
                    original = self.root
                    self.root = node.right
                    self.root.parent = original.parent
                elif node.parent.right is node:
                    original = node
                    node = node.right
                    node.parent = original.parent
                    node.parent.right = node
                else:
                    original = node
                    node = node.right
                    node.parent = original.parent
                    node.parent.left = node
                node.height = 1 + max(self.height(node.left), self.height(node.right))
                node.parent.height = 1 + max(self.height(node.parent.left), self.height(node.parent.right))
                self.rebalance(node)
            elif node.right is None:
                self.size -= 1
                if self.root.value == node.value:
                    original = self.root
                    self.root = node.left
                    self.root.parent = original.parent

                elif node.parent.right is node:
                    original = node
                    node = node.left
                    node.parent = original.parent
                    node.parent.right = node
                else:
                    original = node
                    node = node.left
                    node.parent = original.parent
                    node.parent.left = node
                node.height = 1 + max(self.height(node.left), self.height(node.right))
                node.parent.height = 1 + max(self.height(node.parent.left), self.height(node.parent.right))
                self.rebalance(node)
            else:
                replacement = self.max(node.left)
                node.value = replacement.value

                if self.root is node:
                    if replacement.left:
                        self.size -= 1
                        replacement.left.parent = node
                        node.left = replacement.left

                    else:
                        self.remove(replacement, replacement.value)
                else:
                    self.remove(replacement, replacement.value)

                node.height = 1 + max(self.height(node.left), self.height(node.right))
                #node.parent.height = 1 + max(self.height(node.parent.left), self.height(node.parent.right))
                self.rebalance(node)
        self.rebalance(self.root)
        return self.root

    def search(self, node, value):
        """
        Searches for a specific value within the tree
        :param value: value to search for
        :param node: root of tree/subtree
        :return: node where value was found
        """
        if node is None:
            return None
        if value < node.value:
            if node.left is None:
                return node
            else:
                return self.search(node.left, value)
        elif value > node.value:
            if node.right is None:
                return node
            else:
                return self.search(node.right, value)
        else:
            return node

    def inorder(self, node):
        """
        Traverses tree with inorder method starting at node
        :param node: Node to start traversing
        :return: Generator object of tree traversed
        """

        if node:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)
        else:
            return

    def preorder(self, node):
        """
        Traverses tree with preorder method starting at node
        :param node: Node to start traversing
        :return: Generator object of tree traversed
        """
        if node:
            yield node
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)
        else:
            return

    def postorder(self, node):
        """
        Traverses tree with postorder method starting at node
        :param node: Node to start traversing
        :return: Generator object of tree traversed
        """
        if node:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node
        else:
            return

    def breadth_first(self, node):
        """
        Traverses tree with breadth first method starting at node
        :param node: Node to start traversing
        :return: Generator object of tree traversed
        """
        if node is None:
            return

        my_list = []

        my_list.append(node)

        while (len(my_list) > 0):
            yield my_list[0]
            node = my_list.pop(0)

            if node.left is not None:
                my_list.append(node.left)

            if node.right is not None:
                my_list.append(node.right)

    def depth(self, value):
        """
        Finds the depth of a node with the specific value in the tree
        :param value: Value to find depth of
        :return: Depth of value
        """
        node = self.search(self.root, value)

        if node is None:
            return -1

        elif node.value != value:
            return -1
        else:
            count = 0
            while node.parent:
                count += 1
                node = node.parent
            return count

    def height(self, node):
        """
        Finds the height of the tree rooted at the given node
        :param node: Node to find height of
        :return: Height of node
        """
        if node:
            return node.height
        else:
            return -1

    def min(self, node):
        """
        Finds the minimum value of a tree rooted at the node
        :param node: Root node of tree/subtree to look for minimum value
        :return: Minimum node of tree/subtree
        """
        if self.root is None:
            return None
        else:
            if node.left is None:
                return node
            else:
                return self.min(node.left)

    def max(self, node):
        """
        Finds the maximum value of a tree rooted at the node
        :param node: Root node of tree/subtree to look for maximum valye
        :return: Maximum node of tree/subtree
        """
        if self.root is None:
            return None
        else:
            if node.right is None:
                return node
            else:
                return self.max(node.right)

    def get_size(self):
        """
        Gets size of tree
        :return: number of nodes in tree
        """
        return self.size

    def get_balance(self, node):
        """
        Gets the balance factor of a specific node
        :param node: Node to calculate balance factor of
        :return: balance factor of node
        """
        if node:
            return self.height(node.left) - self.height(node.right)
        else:
            return 0

    def left_rotate(self, root):
        """
        Performs a left rotation of a tree/subtree rooted at root
        :param root: Root location of where left rotation will be performed
        :return: New root of tree/subtree
        """

        y = root.right
        y.parent = root.parent

        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is root:
                y.parent.left = y
            elif y.parent.right is root:
                y.parent.right = y

        root.right = y.left
        if root.right is not None:
            root.right.parent = root
        y.left = root
        root.parent = y

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    def right_rotate(self, root):
        """
        Performs a right rotation of a tree/subtree rooted at root
        :param root: Root location of where right rotation will be performed
        :return: New root of tree/subtree
        """
        y = root.left
        y.parent = root.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is root:
                y.parent.left = y
            elif y.parent.right is root:
                y.parent.right = y
        root.left = y.right
        if root.left is not None:
            root.left.parent = root
        y.right = root
        root.parent = y

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    def rebalance(self, node):
        """
        Rebalances a tree/subtree rooted at node
        :param node: Node to see if it needs to be rebalanced
        :return: New root of balanced tree
        """

        if self.get_balance(node) == -2:
            if self.get_balance(node.right) == 1:
                self.right_rotate(node.right)
            return self.left_rotate(node)

        elif self.get_balance(node) == 2:
            if self.get_balance(node.left) == -1:
                self.left_rotate(node.left)
            return self.right_rotate(node)
        return node


def sum_update(root, total):
    """
    Replaces the keys in the tree with the sum of the keys that are greater than or equal to it, the corrects the tree
    to be a BST
    :param root: root of tree to start at
    :param total: Keeps track of the total keys greater than or equal to root
    :return: the new updated tree
    """

    if root is None:
        return

    sum_update(root.right, total)

    temp = root.value
    total += temp
    root.value = total

    sum_update(root.left, total)

