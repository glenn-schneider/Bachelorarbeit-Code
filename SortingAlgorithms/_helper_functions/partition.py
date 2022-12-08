from SortingAlgorithms._helper_functions.stats import addAccess, addComparison, addShift, addSwap


def medianOfThree(a, b, c, stats, index):
    addComparison(stats, value=4, accesses=0)
    if a <= b <= c or c <= b <= a:
        return index[1]
    addComparison(stats, value=4, accesses=0)
    if b <= a <= c or c <= a <= b:
        return index[0]
    else:
        return index[2]


def median_of_three_partition(arr, left, right, stats=[0, 0, 0]):
    length = right - left
    # find index of median of leftmost, middle and rightmost Element
    median_of_three = medianOfThree(arr[left], arr[left + length // 2 - 1], arr[right], stats,
                                    index=[left, left + length // 2 - 1, right])
    addAccess(stats, value=3)

    # Move median to the front
    arr[left], arr[median_of_three] = arr[median_of_three], arr[left]
    addSwap(stats)

    # make first element (median of three) the pivot element
    pivot = left
    i = left + 1

    # Go through given array range
    for j in range(left + 1, right + 1):
        # if element less than or equal to pivot element: increase index i and swap that element with element at index i
        if arr[j] <= arr[pivot]:
            # addComparison(stats)
            arr[i], arr[j] = arr[j], arr[i]
            addSwap(stats)
            i += 1
    # Compare every element except the pivot once:
    addComparison(stats, value=length - 1, accesses=((length - 1) * 2))

    # Move the pivot element to its correct position.
    # Everything to the left is less than the pivot and everything to the right is larger than the pivot.
    arr[i - 1], arr[pivot] = arr[pivot], arr[i - 1]
    addSwap(stats)
    pivot = i - 1

    return pivot
