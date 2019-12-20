"""
PROJECT 3 - Quick/Insertion Sort
Name: Hailey Reese
PID: A50227795
"""

from Project3.InsertionSort import insertion_sort


def quick_sort(dll, start, end, size, threshold):
    """
    Sorts a linked list with the quick sort algorithm, unless the threshold is underpassed
    :param dll: doubly linked list to sort
    :param start: node to start sorting at
    :param end: node to stop sorting at
    :param size: size of linked list
    :param threshold: integer used to determine if quick or insertion sort should be used
    """
    if size <= 1:
        return
    if size < threshold:
        insertion_sort(dll, start, end)
    else:
        p = partition(start, end)
        pivot = p[0]
        new_size1 = p[1]
        new_size2 = size - new_size1 - 1
        quick_sort(dll, start, pivot.get_previous(), new_size1, threshold)
        quick_sort(dll, pivot.get_next(), end, new_size2, threshold)


def partition(low, high):
    """
    Partitions the linked list by moving any values less than the pivot to the left, and all others to the right
    :param low: node to start partitioning at
    :param high: node to stop partitioning at
    :return: tuple of pivot node and new size from start to pivot node
    """
    pivot = high.get_value()
    left = low.get_previous()
    right = low
    count = 0
    while right is not high:
        if right.get_value() < pivot:
            if left is None:
                left = low
            else:
                left = left.get_next()
            temp = left.get_value()
            left.set_value(right.get_value())
            right.set_value(temp)
            count += 1
        right = right.get_next()

    if left is None:
        left = low
    else:
        left = left.get_next()
    temp = left.get_value()
    left.set_value(high.get_value())
    high.set_value(temp)
    return (left, count)