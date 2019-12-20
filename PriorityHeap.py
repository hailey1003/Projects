class Node:
    """
    Node definition should not be changed in any way
    """
    __slots__ = ['_key', '_value']

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self._key = k
        self._value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False if otherwise
        """
        return self._key < other.get_key() or (self._key == other.get_key() and self._value < other.get_value())

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False if otherwise
        """
        return self._key > other.get_key() or (self._key == other.get_key() and self._value > other.get_value())

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False if otherwise
        """
        return self._key == other.get_key() and self._value == other.get_value()

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self._key, self._value)

    __repr__ = __str__

    def get_key(self):
        """
        Key getter function
        :return: key value of the node
        """
        return self._key

    def set_key(self, new_key):
        """
        Key setter function
        :param new_key: the value the key is to be changed to
        """
        self._key = new_key

    def get_value(self):
        """
        Value getter function
        :return: value of the node
        """
        return self._value


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = '_data'

    def __init__(self):
        """
        Initializes the priority heap
        """
        self._data = []

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Modify below this line

    def empty(self):
        """
        Checks if priority queue is empty
        :return: Bool: True if empty, False if not
        """
        return (self._data == [])

    def top(self):
        """
        Gives the root value of heap
        :return: The value of the root
        """
        if self._data == []:
            return None
        else:
            return self._data[0].get_value()



    def push(self, key, val):
        """
        Adds a node to the heap with specific key and value
        :param key: the priority of the node in order to know where it should be added
        :param val: value of the node that is being added
        :return: None
        """
        new = Node(key, val)
        self._data.append(new)
        self.percolate_up(len(self._data) -  1)


    def pop(self):
        """
        Removes the smallest element from priority queue
        :return: The node that was removed
        """
        if len(self._data) == 0:
            return None
        else:
            temp = self._data[len(self._data)-1]
            self._data[len(self._data)-1] = self._data[0]
            self._data[0] = temp
            item = self._data.pop()
            self.percolate_down(0)
            return item

    def min_child(self, index):
        """
        Returns the smaller child of a given index of node
        :param index: Index of node to find smallest child
        :return: Smallest child of the indexed node
        """

        left_child = int(2 * index + 1)
        right_child = int(2 * index + 2)

        if len(self._data) == 0 or len(self._data) == 1:
            return None
        elif left_child >= len(self._data) and right_child >= len(self._data):
            return None
        else:
            if left_child < len(self._data):
                small = left_child
            if right_child < len(self._data) and self._data[right_child] < self._data[left_child]:
                small = right_child
            return small

    def percolate_up(self, index):
        """
        Moves a specific node up to its valid spot
        :param index: Index of node to move up
        :return: None
        """
        while index > 0:
            parent_index = int((index - 1) / 2)
            key = self._data[index].get_key()
            parent_key = self._data[parent_index].get_key()
            value = self._data[index].get_value()
            parent_value = self._data[parent_index].get_value()
            if (key > parent_key) or (key == parent_key and value > parent_value):
                return
            elif (key < parent_key) or (key == parent_key and value < parent_value):
                temp = self._data[index]
                self._data[index] = self._data[parent_index]
                self._data[parent_index] = temp
                index = parent_index
            else:
                index = parent_index

    def percolate_down(self, index):
        """
        Moves a specific node down to its valid spot
        :param index: Index of node to move down
        :return: None
        """
        smallest = index
        left_child = int(2 * index+1)
        right_child = int(2 * index + 2)

        if left_child < len(self._data) and self._data[smallest] > self._data[left_child]:
            smallest = left_child
        if right_child < len(self._data) and self._data[smallest] > self._data[right_child]:
            smallest = right_child
        if smallest != index:
            temp = self._data[index]
            self._data[index] = self._data[smallest]
            self._data[smallest] = temp
            self.percolate_down(smallest)

    def change_priority(self, index, new_key):
        """
        Changes the priority of the node at the given index to the given value
        :param index: index of node whose key needs to be changed
        :param new_key: new key value of node
        :return: None
        """
        if index >= len(self._data):
            return
        old_key = self._data[index].get_key()
        self._data[index].set_key(new_key)
        if old_key > new_key:
            self.percolate_up(index)
        else:
            self.percolate_down(index)


def heap_sort(array):
    """
    Utilizing the heap sort algorithm to sort the data
    :param array: Array of data that needs to be turned into a heap to sort
    :return: List of new sorted data
    """
    if len(array) == 0:
        return []
    elif len(array) == 1:
        new_list = []
        item = array[0]
        new_list.append(item)
        return new_list
    else:
        heap = PriorityHeap()

        for i in range(0, len(array)):
            key = array[i]
            value = array[i]
            heap.push(key, value)

        new_list = []
        for i in range(len(heap)):
            item = heap.pop()
            value = item.get_value()
            new_list.append(value)
        return new_list


def merge_lists(array_list):
    """
    Merge all the lists given in parameter into one single sorted list
    :param array_list: list of unsorted lists
    :return: a single list of sorted data
    """
    return_list = []
    new_array = array_list
    for i in range(len(array_list)):
        item = heap_sort(array_list[i])
        new_array[i] = item

    new_heap = PriorityHeap()

    for i in range(len(new_array)):
        if len(new_array[i]) != 0:
            new_heap.push(new_array[i][0], i)
            new_array[i].pop(0)

    while len(new_heap) != 0:
        item = new_heap.pop()
        value = item.get_key()
        array_index = item.get_value()

        if value not in return_list:
            return_list.append(value)

        if len(new_array[array_index]) != 0:
            new_heap.push(new_array[array_index][0], array_index)
            new_array[array_index].pop(0)

    return return_list
