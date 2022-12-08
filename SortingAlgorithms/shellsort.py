from SortingAlgorithms._helper_functions.stats import addAccess, addComparison, addShift, addSwap
from math import ceil


# Find gaps using Tokuda's Sequence
def find_gaps(n):
    gaps = []
    k = 1
    while True:
        hk = ceil((1 / 5) * (9 * ((9 / 4) ** (k - 1)) - 4))
        k += 1
        if hk < n:
            gaps.insert(0, hk)
        else:
            return gaps


def shellsort(arr, stats):
    n = len(arr)
    # get a list of the gaps for the shellsort
    gaps = find_gaps(n)
    # for every gap, do an insertion sort on gapped elements
    for gap in gaps:
        # Find correct gap spot for each element.
        for i in range(gap, n):
            # hold arr[i] in a temp variable until correct spot for it is found
            temp = arr[i]
            # addAccess(stats)

            j = i
            # shift all elements to the left of i that are multiples of gap away, until right spot for element is found.
            addComparison(stats, accesses=1)
            while j >= gap and arr[j - gap] > temp:
                addComparison(stats, accesses=1)
                arr[j] = arr[j - gap]
                addShift(stats, accesses=2)
                j -= gap

            # move held variable into its correct spot. If i==j, then its already in the correct spot
            if i != j:
                arr[j] = temp
                addSwap(stats, accesses=1, shifts=1)

        # Every Element between gap and n gets saved in a temp variable once:
        addAccess(stats, value=n - gap)
