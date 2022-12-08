from SortingAlgorithms._helper_functions.stats import addAccess, addComparison, addShift, addSwap


def insertionsort(arr, left=0, right=None, stats=[0, 0, 0]):
    # if no bounds set, do insertionsort on entire list
    if right is None:
        right = len(arr) - 1

    # for every element in the list, find its correct spot
    for i in range(left + 1, right + 1):
        key = arr[i]
        addAccess(stats)
        j = i - 1

        # compare key with each number to the left until you a number smaller than the key is found
        # move larger numbers up
        while j >= left and key < arr[j]:
            # addComparison(stats, accesses = 1)
            arr[j + 1] = arr[j]
            # addShift(stats, accesses = 2)
            j -= 1
        # collect stats outside the loop to save time. When the loop stops the key was compared with i-j Elements,
        # and i-j-1 Elements were shifted up
        addComparison(stats, value=i - j, accesses=i - j)
        addShift(stats, value=i - j - 1, accesses=(i - j - 1) * 2)

        # move held element to its correct spot. Not a swap if element didn't move
        if i != j:
            arr[j + 1] = key
            addSwap(stats, accesses=1)
