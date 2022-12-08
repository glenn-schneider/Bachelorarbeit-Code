from SortingAlgorithms._helper_functions.insertionsort import insertionsort
from SortingAlgorithms._helper_functions.stats import addAccess, addComparison, addShift, addSwap


def smallest_largest(a, stats):
    length = len(a)
    # initialize minimum and maximum Element as first Element of List
    amin = a[0]
    addAccess(stats)
    amax = a[0]
    addAccess(stats)

    # go through the list and find the index of the smallest and largest number
    for i in range(0, length):
        elem = a[i]
        # addAccess(stats)
        # addComparison(stats, accesses=1)
        if elem < a[amin]:
            amin = i
        # addComparison(stats, accesses=1)
        if elem > a[amax]:
            amax = i
    # Every Element got saved in a temp value once.
    addAccess(stats, value=length)
    # Every value got compared to the current min and max one time each
    addComparison(stats, value=2 * length, accesses=2 * length)

    return (amin, amax)


def flashsort(a, stats):
    # ----- Classification -----
    n = len(a)

    # using the "optimal" number of buckets m assuming shifts are twice as expensive as comparisons
    m = int(0.43 * n)

    # find the index of the smallest and largest elements:
    min_max = smallest_largest(a, stats)

    amin = a[min_max[0]]
    amax = a[min_max[1]]
    addAccess(stats, value=2)

    # compute once and reuse later
    c1 = (m - 1) / (amax - amin)

    # create a list and check how many items go into each class K. K(A(i)) = INT((m-1)(A(i)-Amin)/(Amax-Amin))
    l = [0] * m
    for i in range(0, n):
        l[int(c1 * (a[i] - amin))] += 1
        # addAccess(stats)
    # accessed each element once
    addAccess(stats, value=n)

    # make l a prefix sum where l[j] is the number of elements in classes K(j<=i)
    for i in range(1, m):
        l[i] += l[i - 1]

    # Save copy of this for bounds for insertionsort later
    l2 = [0] + l[:]

    # ----- Permutation -----
    moves = 0
    j = 0
    k = m - 1

    # Each element is moved once so stop after n moves
    while moves < n - 1:
        # Find new cycle leader. Do this by finding an element that isn't in its correct class.
        addAccess(stats)
        while j > l[k] - 1:
            j += 1
            k = int(c1 * (a[j] - amin))
            addAccess(stats)

        flash = a[j]
        addAccess(stats)

        # Move the element flash into its correct class by swapping. The swapped element becomes the new flash.
        # If the swapped Element is swapped into its correct class, find a new cycle leader.
        while j != l[k]:
            k = int(c1 * (flash - amin))
            a[l[k] - 1], flash = flash, a[l[k] - 1]
            addSwap(stats, shifts=1, accesses=2)

            l[k] = l[k] - 1
            addShift(stats, accesses=2)

            moves += 1

    # ----- Insertion -----
    # Do a regular Insertionsort on each Class
    for i in range(1, m):
        insertionsort(a, left=l2[i - 1], right=l2[i] - 1, stats=stats)
