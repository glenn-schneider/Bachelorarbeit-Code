from math import log, floor

from SortingAlgorithms._helper_functions.heapsort import heapsort
from SortingAlgorithms._helper_functions.insertionsort import insertionsort
from SortingAlgorithms._helper_functions.partition import median_of_three_partition
from SortingAlgorithms._helper_functions.stats import addAccess, addComparison, addShift


def introsort(arr, threshold=10, maxdepth=None, stats=[0, 0, 0, 0]):
    if maxdepth == None:
        maxdepth = 2 * floor(log(len(arr)))
    introsort_helper(arr, 0, len(arr) - 1, threshold, maxdepth, stats)


def introsort_helper(arr, left, right, threshold, maxdepth, stats):
    size = right - left

    # if List is smaller than threshold, use insertionsort
    if size < threshold:
        insertionsort(arr, left, right, stats)
        return

    # if maxdepth is reached, use heapsort
    if maxdepth == 0:
        heapsort(arr, left, right, stats)
        return

    # if list is larger than threshold and maxdepth isn't reached yet, use quicksort
    else:
        # find pivot using the median-of-three and partition the list
        pivot = median_of_three_partition(arr, left, right, stats)

        introsort_helper(arr, left, pivot - 1, threshold, maxdepth - 1, stats)
        introsort_helper(arr, pivot + 1, right, threshold, maxdepth - 1, stats)
