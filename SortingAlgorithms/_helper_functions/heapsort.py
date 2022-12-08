from SortingAlgorithms._helper_functions.stats import addAccess, addComparison, addShift, addSwap


def build_max_heap(arr, left, right, stats):
    size = right - left
    # start is the position of the parent of the last element in the heap
    start = (size - 2) // 2

    # move up in the tree until all subtrees fulfill heapify
    for i in range(start, -1, -1):
        heapify(arr, i, left, right, stats)


def heapify(arr, index, left, right, stats):
    size = right - left

    # children for subtree starting at index:
    l = 2 * index + 1
    r = 2 * index + 2

    # set root as largest element
    largest = index

    # if left child exists and is larger than root, l is largest
    if l < size and arr[left + l] > arr[left + index]:
        largest = l
    addComparison(stats, accesses=2)

    # if right child exists and is larger than root, r is largest
    if r < size and arr[left + r] > arr[left + largest]:
        largest = r
    addComparison(stats, accesses=2)

    # if root isn't the largest element, swap root with largest element
    # Run heapify on subtree until root is larger than both children
    if largest != index:
        arr[left + largest], arr[left + index] = arr[left + index], arr[left + largest]
        addSwap(stats)
        heapify(arr, largest, left, right, stats)


def heapsort(arr, left=0, right=None, stats=[0, 0, 0]):
    # if no bounds set, do heapsort on entire list
    if right is None:
        right = len(arr) - 1

    length = right - left

    # First, build a max heap
    build_max_heap(arr, left, right + 1, stats)

    # Take largest element of list and put it to the end. That element is now sorted.
    # Run heapify again to get the largest element to the root again
    for i in range(right, left, -1):
        arr[i], arr[left] = arr[left], arr[i]
        # addSwap(stats)
        heapify(arr, index=0, left=left, right=i, stats=stats)
    # one swap for each element
    addSwap(stats, value=length, accesses=4 * length)
