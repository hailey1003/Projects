"""
PROJECT 3 - Quick/Insertion Sort
Name: Hailey Reese
PID: A50227795
"""
def _insertion_wrapper(insertion_sort):
    """
    DO NOT EDIT
    :return:
    """
    def insertion_counter(*args, **kwargs):
        if args[0].size > 1:
            args[0].c += 1
        insertion_sort(*args, **kwargs)
    return insertion_counter

# ------------------------Complete function below---------------------------
@_insertion_wrapper
def insertion_sort(dll, low, high):
    """
    Sorts a linked list using the insertion sort algorithm
    :param dll: doubly linked list to sort
    :param low: node to start sorting at
    :param high: node to stop sorting at
    """
    if dll.get_size() == 0 or dll.get_size() == 1:
        return
    current = low.get_next()
    while current != high.get_next():
        while current.get_previous() != None and current.get_previous().get_value() > current.get_value():
            temp = current.get_value()
            current.set_value(current.get_previous().get_value())
            current.get_previous().set_value(temp)
            current = current.get_previous()
        current = current.get_next()

