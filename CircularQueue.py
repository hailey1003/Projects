"""
Project 4- Solution
"""


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.total = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size and self.total == \
               other.get_total()

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"
        result = ""
        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + (", ").join(str_list)

    # -----------MODIFY BELOW--------------

    def is_empty(self):
        """
        Returns whether or not the queue is empty
        :return: True if empty, False if not
        """
        return bool(self.size == 0)

    def __len__(self):
        """
        Returns the size of the queue
        :return: size of queue int
        """
        return self.size

    def get_total(self):
        """
        Returns the sum of all the elements in the queue
        :return: total sum
        """
        return self.total

    def head_element(self):
        """
        Returns the front element of the queue
        :return: head element of queue
        """
        return self.data[self.head]

    def tail_element(self):
        """
        Returns the last element of the queue
        :return: tail element of the queue
        """
        return self.data[self.tail-1]

    def enqueue(self, val):
        """
        Adding a value to the back of the queue
        :param val: Value we want to add
        """
        if self.size == 0:
            self.data[self.tail] = val
            self.total += val
            self.tail += 1
        else:
            self.data[self.tail] = val
            self.total += val
            self.tail += 1
        self.size += 1
        if self.size == self.capacity:
            self.grow()

    def dequeue(self):
        """
        Remove an element from the front of queue
        :return: Element we deleted or None if queue is empty,
        """
        if self.is_empty():
            return None
        answer = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        self.total -= answer

        if self.size <= (1 / 4) * self.capacity and self.capacity > 4:
            self.shrink()

        return answer

    def grow(self):
        """
        Doubles capacity of the queue when capacity is reached
        """
        old = self.data
        self.capacity = 2 * self.capacity
        self.data = [None] * self.capacity
        walk = self.head
        for i in range(self.size):
            self.data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self.head = 0

    def shrink(self):
        """
        Halves the capacity of the queue when size is less than 1/4 of capacity
        """
        old = self.data
        if self.capacity < 4:
            self.capacity = 4
        elif self.capacity == 5:
            self.capacity = 5
        else:
            self.capacity = int((1 / 2) * self.capacity)
        self.data = [None] * self.capacity
        walk = self.head
        for i in range(self.size):
            self.data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self.head = 0
        self.tail = self.size


def threshold_sum(nums, threshold):
    """
    Finds the sequence of consecutive numbers in nums with the highest possible sum less than or equal to the threshold
    :param nums: sequence of consecutive numbers
    :param threshold: sum that the consecutive numbers cannot be greater than
    :return: a tuple with the sum of consecutive numbers and the length
    """
    queue = CircularQueue(len(nums))
    for i in range(len(nums)):
        queue.enqueue(nums[i])
        the_sum = queue.get_total()
        if the_sum > threshold:
            queue.dequeue()

    if the_sum > threshold:
        queue.dequeue()

    if queue.is_empty():
        return (0, 0)
    else:
        return (queue.get_total(), queue.size)
