"""
CSE 331 Project 1
Author: Hailey Reese
"""
import math
class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next = None, prev = None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.__next = next
        self.__prev = prev
        self.__value = value

    def __repr__(self):
        return str(self.__value)

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        """
        Getter for value
        :return: the value of the node
        """
        return self.__value

    def set_value(self, value):
        """
        Setter for value
        :param value: the value to set
        """
        self.__value = value

    def get_next(self):
        """
        Getter for next node
        :return: the next node
        """
        return self.__next

    def set_next(self, node):
        """
        Setter for next node
        :param node: the node to set
        """
        self.__next = node

    def get_previous(self):
        """
        Getter for previous node
        :return: the previous node
        """
        return self.__prev

    def set_previous(self, node):
        """
        Setter for previous node
        :param node: the node to set
        """
        self.__prev = node

class DLL:
    """
    Class representing a doubly linked list.
    """
    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.get_next():
                res += " "
            node = node.get_next()
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.get_next():
                res += " "
            node = node.get_next()
        return res

    ######### MODIFY BELOW ##########

    def get_size(self):
        """
        Gives the user the size of their linked list
        :return: [int] the size of the linked list
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        boolean = bool(self.size == 0)
        #if self.size == 0:
            #boolean = True
        #else:
            #boolean = False
        return boolean

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        """
        new_node = DLLNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node
            self.size += 1

    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        new_node = DLLNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.set_previous(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            self.size += 1

    def delete_front(self):
        """
        Deletes the front node of the list
        """
        if self.head is None:
            return
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            next_node = self.head.get_next()
            next_node.set_previous(None)
            self.head = next_node
            self.size -= 1

    def delete_back(self):
        """
        Deletes the back node of the list
        """
        if self.head is not None:
            if self.head != self.tail:
                prev_node = self.tail.get_previous()
                self.tail = prev_node
                self.tail.set_next(None)
            else:
                self.head = None
                self.tail = None
            self.size -= 1

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        node_to_remove = self.find_first(value)
        if node_to_remove == self.head:
            self.delete_front()
        elif node_to_remove == self.tail:
            self.delete_back()
        else:
            next_val = node_to_remove.get_next()
            prev_val = node_to_remove.get_previous()
            prev_val.set_next(next_val)
            next_val.set_previous(prev_val)
            self.size -= 1

    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        the_node = self.head
        while the_node:
            if the_node.get_value() == value:
                self.delete_value(value)
            the_node = the_node.get_next()

    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """
        node = self.head
        while node:
            if node.get_value() == value:
                return node
            else:
                node = node.get_next()

    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """
        node = self.tail
        while node:
            if node.get_value() == value:
                return node
            else:
                node = node.get_previous()

    def find_all(self, value):
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """
        the_list = []
        node = self.head
        while node:
            if node.get_value() == value:
                the_list.append(node)
            node = node.get_next()
        return the_list

    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        the_list = self.find_all(value)
        count = len(the_list)
        return count

    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """

        the_node = self.head
        if the_node is None:
            new_variable = None
        else:
            first_value = the_node.get_value()
            the_type = type(first_value)
            new_variable = the_type()
            while the_node:
                number = the_node.get_value()
                new_variable += number
                the_node = the_node.get_next()
        return new_variable

def remove_middle(LL):
    """
    Removes the middle of a given doubly linked list.
    :param DLL: The doubly linked list that must be modified
    :return: The updated linked list
    """
    length = LL.get_size()
    if length == 0:
        LL = LL
    elif length == 1:
        LL.head = None
        LL.tail = None
        LL.size -= 1
    elif length == 2:
        LL.head = None
        LL.tail = None
        LL.size -= 2
    else:
        if length % 2 == 0:
            first_middle_node = length / 2
            position = 1
            the_node = LL.head
            while the_node:
                if position == first_middle_node:
                    prev_node = the_node.get_previous()
                    next_node = the_node.get_next()
                    next_next_node = next_node.get_next()
                    prev_node.set_next(next_next_node)
                    next_next_node.set_previous(prev_node)
                    LL.size -= 2
                the_node = the_node.get_next()
                position += 1
        else:
            middle_node = math.ceil(length / 2)
            position = 1
            the_node = LL.head
            while the_node:
                if position == middle_node:
                    next_node = the_node.get_next()
                    prev_node = the_node.get_previous()
                    next_node.set_previous(prev_node)
                    prev_node.set_next(next_node)
                    LL.size -= 1
                the_node = the_node.get_next()
                position += 1
    return LL
