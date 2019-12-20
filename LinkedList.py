"""
PROJECT 2 - Linked List Recursion
Name: Hailey Reese
PID: A50227795
"""


class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self.value = value  # element at the node
        self.next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #


def insert(value, node=None):
    """
    Inserts param value at the end of list
    :param value: value of the node to be inserted into list
    :param node: head node of the list
    :return: head node of the list 
    """
    new_node = LinkedNode(value)
    if node is None:
        node = new_node
    else:
        node.next = insert(value, node.next)
    return node


def to_string(node):
    """
    Converts the all the elements of the list into a single string
    :param node: head node of the list
    :return: string representation of list
    """
    if node is None:
        the_string = ''
    else:
        if node.next is None:
            the_string = str(node.value)
        else:
            the_string = str(node.value) + ', '
            the_string = the_string + to_string(node.next)
    return the_string

def remove(value, node):
    """
    Removes the first occurance of a specific value from list
    :param value: value of the node to be removed
    :param node: head node of the list
    :return: head node of the list 
    """
    if node is None:
        return None
    elif node.next is None:
        if node.value == value:
            return None
    else:
        if node.value == value:
            node = node.next
        else:
            node.next = remove(value, node.next)
    return node

def remove_all(value, node):
    """
    Removes all occurrences of a specific value from list
    :param value: value of the node to be removed
    :param node: head node of the list
    :return: head node of the list
    """
    if node is None:
        return None
    elif node.next is None:
        if node.value == value:
            node = None
    else:
        if node.value == value:
            node = node.next
            node = remove_all(value, node)
        else:
            node.next = remove_all(value, node.next)
    return node

def search(value, node):
    """
    Searches through list to see if value is actually in the list
    :param value: value of the node to search for
    :param node: head node of the list
    :return: boolean value: True if value is in list, False if value is not
    """
    if node is None:
        t_value = False
    elif node.value == value:
        t_value = True
    else:
        t_value = search(value, node.next)
    return t_value


def length(node):
    """
    Calculates the length of the list
    :param node: head node of the list
    :return: length of list
    """
    if node is None:
        the_length = 0
    else:
        the_length = 1 + length(node.next)
    return the_length


def sum_list(node):
    """
    Calculates the sum of all the values in the list
    :param node: head node of the list
    :return: sum of the list
    """
    if node is None:
        the_sum = 0
    else:
        the_sum = node.value + sum_list(node.next)
    return the_sum


def count(value, node):
    """
    Counts the number of times a value occurs in the list
    :param value: value of the node to count
    :param node: head node of the list
    :return: the count of occurrences
    """
    if node is None:
        the_count = 0
    elif node.value == value:
        the_count = 1 + count(value, node.next)
    else:
        the_count = 0 + count(value, node.next)
    return the_count

def reverse(node):
    """
    Reverses the order of nodes in the list
    :param node: head node of the list
    :return: new head node of the list
    """
    if node is None:
        return None
    elif node.next is None:
        return node
    else:
        a_node = reverse(node.next)
        temp = node.next
        temp.next = node
        node.next = None
        node = temp
        return a_node


def remove_fake_requests(head):
    """
    Removes any duplicates within the list
    :param head: head node of the list
    :return: head node of the list
    """
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        if head.value == head.next.value:
            temp = head.next
            while (temp is not None) and (head.value == temp.value):
                head.next = None
                temp = temp.next
            return remove_fake_requests(temp)
        else:
            head.next = remove_fake_requests(head.next)
            return head
        

def main():
    requests = insert(123456)
    insert(123456, requests)
    insert(123456, requests)
    requests = remove_fake_requests(requests)
    print(to_string(requests))
main()