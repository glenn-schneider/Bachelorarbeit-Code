from SortingAlgorithms._helper_functions.partition import median_of_three_partition
from SortingAlgorithms._helper_functions.stats import addAccess, addComparison, addShift


def quicksort(arr, left=0, right=None, stats=[0, 0, 0]):
    # if no bounds set, do quicksort on entire list
    if right is None:
        right = len(arr) - 1

    if left < right:
        # Get the pivot element and partition using the median-of-three
        pivot = median_of_three_partition(arr, left, right, stats)

        # Repeat Quicksort on left and right sublists
        quicksort(arr, left, pivot - 1, stats)
        quicksort(arr, pivot + 1, right, stats)
