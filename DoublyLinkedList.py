"""
PROJECT 3 - Quick/Insertion Sort
Name: Hailey Reese
PID: A50227795
"""

from Project3.QuickSort import quick_sort


class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        DO NOT EDIT
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.__next = next
        self.__prev = prev
        self.__value = value

    def __str__(self):
        """
        DO NOT EDIT
        String representation of node
        :return: string of node's value
        """
        return str(self.__value)

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.__value == other.__value:
            return True
        return False

    def get_value(self):
        """
        DO NOT EDIT
        Getter for value
        :return: the value of the node
        """
        return self.__value

    def set_value(self, value):
        """
        DO NOT EDIT
        Setter for value
        :param value: the value to set
        """
        self.__value = value

    def get_next(self):
        """
        DO NOT EDIT
        Getter for next node
        :return: the next node
        """
        return self.__next

    def set_next(self, node):
        """
        DO NOT EDIT
        Setter for next node
        :param node: the node to set
        """
        self.__next = node

    def get_previous(self):
        """
        DO NOT EDIT
        Getter for previous node
        :return: the previous node
        """
        return self.__prev

    def set_previous(self, node):
        """
        DO NOT EDIT
        Setter for previous node
        :param node: the node to set
        """
        self.__prev = node


class DLL:
    """
    Class representing a doubly linked list.
    """
    c = 0

    def __init__(self, data=None):
        """
        DO NOT EDIT
        Constructor
        :param: data to initialize list
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

        if data:
            [self.insert_back(i) for i in data]

    def __str__(self):
        """
        DO NOT EDIT
        String representation of a doubly linked list showing prev and next nodes
        :return: string of linked list
        """
        result = ""
        node = self.head

        while node:
            prev = "None"
            nxt = "None"

            if node.get_previous():
                prev = str(node.get_previous().get_value())

            if node.get_next():
                nxt = str(node.get_next().get_value())

            result += str(node.get_value()) + " (" + prev + ", " + nxt + ") " + "-> "
            node = node.get_next()

        return result + "None"

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size or self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other and temp_self.get_previous() == temp_other.get_previous():
                temp_self = temp_self.get_next()
                temp_other = temp_other.get_next()
            else:
                return False

        # Make sure both are not longer than the other
        if temp_self is None and temp_other is None:
            return True

        return False

    def get_head(self):
        """
        DO NOT EDIT
        Getter for tail
        :return: tail node
        """
        return self.head

    def set_head(self, node):
        """
        DO NOT EDIT
        Setter for head
        :param node: node to assign to head
        """
        self.head = node

    def get_tail(self):
        """
        DO NOT EDIT
        Getter for tail
        :return: tail node
        """
        return self.tail

    def set_tail(self, node):
        """
        DO NOT EDIT
        Setter for tail
        :param node: node to assign to tail
        """
        self.tail = node

    def is_empty(self):
        """
        DO NOT EDIT
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        return self.head is None and self.tail is None

    def get_size(self):
        """
        DO NOT EDIT
        Gives the user the size of their linked list
        :return: [int] the size of the linked list
        """
        return self.size

    def insert_back(self, value):
        """
        DO NOT EDIT
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        node = DLLNode(value, prev=self.tail)
        if self.tail:
            self.tail.set_next(node)
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    # ------------------------Complete function below---------------------------

    def count_unique(self):
        quick_sort(self, self.head, self.tail, self.get_size(), 1)
        rpoint = self.head
        wpoint = self.head
        count1 = 1
        count2 = 0
        while rpoint.get_next() is not None:
            if rpoint == rpoint.get_next():
                count1 += 1
            else:
                wpoint.set_value(rpoint.get_value())
                self.size -= 1
                wpoint = wpoint.get_next()
                if count1 > 1:
                    count_str = str(count1)
                    for i in count_str:
                        wpoint.set_value(int(i))
                        wpoint = wpoint.get_next()
                        self.size += 1
                count1 = 1
                count2 += 1
            rpoint = rpoint.get_next()
        if self.head == self.tail:
            self.tail.set_value(count1)
            self.head.set_next(self.tail)
            self.tail.set_previous(self.head)
            self.size = 2
        if count1 > 1:
            wpoint.get_next().set_next(None)
