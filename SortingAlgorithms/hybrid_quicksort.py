from SortingAlgorithms._helper_functions.insertionsort import insertionsort
from SortingAlgorithms._helper_functions.partition import median_of_three_partition
from SortingAlgorithms._helper_functions.stats import addAccess, addComparison, addShift


def hybrid_quicksort(arr, left=0, right=None, threshold=10, stats=[0, 0, 0]):
    # if no bounds set, do advanced quicksort on entire list
    if right is None:
        right = len(arr) - 1

    if left < right:
        # if array is larger than threshold use quicksort
        if right - left >= threshold:
            pivot = median_of_three_partition(arr, left, right, stats)

            hybrid_quicksort(arr, left, pivot - 1, threshold, stats)
            hybrid_quicksort(arr, pivot + 1, right, threshold, stats)

        else:
            insertionsort(arr, left, right, stats)
