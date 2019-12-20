"""
Project 7 - Hash Tables
CSE331 - F19
Created By: Wendy Fogland
"""


class HashNode:
    """
    DO NOT EDIT
    """

    def __init__(self, key, value, available=False):
        self.key = key
        self.value = value
        self.is_available = available

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=7):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: how much the hash table can hold
        """

        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        for prime in self.primes:
            if self.capacity <= prime:
                self.prime = prime
                break

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """

        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """

        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def _is_available(self, j):
        """
        DO NOT EDIT
        Check if the index in the table is available/empty
        :param j: index in the table
        :return: True if available or empty, false otherwise
        """
        return self.table[j] is None or self.table[j].is_available is True

    def hash_first(self, key):
        """
        DO NOT EDIT
        Converts key, a string, into a bin number for the hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if val is an empty string
        """

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def hash_second(self, key):
        """
        Hashes key based on prime number for double hashing
        DO NOT EDIT
        :param key: key to be hashed
        :return: a hashed value
        """

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        hashed_value = self.prime - (hashed_value % self.prime)
        if hashed_value % 2 == 0:
            hashed_value += 1

        return hashed_value

    def double_hashing(self, key, inserting=False):
        """
        Finds index of where a key can be inseryed into table based off if there is a collision or not
        :param key: key to be hashed
        :return:  index in which the key can be inserted into the hash table
        """
        first = self.hash_first(key)

        if self.table[first] is None:  # if first bin is empty return that number
            return first

        elif self.table[first].key == key:  # key already exists???
            return first

        else:  # collision
            for i in range(self.capacity):
                double = (self.hash_first(key) + i * self.hash_second(
                    key)) % self.capacity  # find double hashing bin number
                # print(double)
                if self.table[double] is None:
                    # print(double)
                    return double

    def insert(self, key, value):
        """
        Use the key and value parameters to add a HashNode to the hash table.
        :param key: key to be inserted
        :param value: associated value to be inserted with key
        :return:  None
        """
        index = self.double_hashing(key, inserting=True)
        node = HashNode(key, value)

        if self._is_available(index) is True:
            self.table[index] = node
            self.size += 1
        elif self.table[index].key == key:
            self.table[index].value = value

        load_factor = self.size / self.capacity
        if load_factor >= 0.4:
            self.grow()

    def search(self, key):
        """
        Searches the Hash Table to find given key
        :param key: key to be searched for
        :return:  None if key is not found. Node key is at if it is found
        """

        for i in range(self.capacity):
            if self.table[i] is not None:
                if self.table[i].key == key:
                    return self.table[i]

    def grow(self):
        """
        Increases the capacity of the existing hash table and rehashes nodes in table
        :return:  None
        """
        self.capacity *= 2
        for prime in self.primes:
            if self.capacity < prime:
                self.prime = prime
                break
        self.rehash()

    def rehash(self):
        """
        Rehashes all nodes in table
        :return:  None
        """
        old_hash = self.table
        self.size = 0
        self.table = [None] * self.capacity
        for i in range(len(old_hash)):
            if old_hash[i] is not None:
                self.insert(old_hash[i].key, old_hash[i].value)

    def delete(self, key):
        """
        Removes the HashNode with the given key from the hash table
        :param key:  key of the node to delete
        :return:  None
        """
        node_to_delete = self.search(key)
        if node_to_delete is not None:
            node_to_delete.key = None
            node_to_delete.value = None
            node_to_delete.is_available = True
            self.size -= 1


def anagrams(string1, string2):
    """
    Determines if the two strings are anagrams
    :param string1:  first string to compare to second string
    :param string2: second string to compare to the first
    :return:  True if they are anagrams, false if they are not
    """
    string1 = string1.lower()
    string2 = string2.lower()
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    ht = HashTable()

    for i in range(len(string1)):
        key = string1[i]
        value = 1

        node = ht.search(key)

        if node is None:
            ht.insert(string1[i], value)
        else:
            value = node.value + 1
            ht.insert(string1[i], value)

    ht2 = HashTable(1)
    for j in range(len(string2)):
        key = string2[j]
        value = 1

        node = ht2.search(key)

        if node is None:
            ht2.insert(string2[j], value)
        else:
            value = node.value + 1
            ht2.insert(string2[j], value)

    for ele in ht.table:
        if ele is not None:
            found = ht2.search(ele.key)
            if found is None:
                return False
            elif found.value != ele.value:
                return False
            else:
                continue

    for ele in ht2.table:
        if ele is not None:
            found = ht.search(ele.key)
            if found is None:
                return False
            elif found.value != ele.value:
                return False
            else:
                continue
    return True
