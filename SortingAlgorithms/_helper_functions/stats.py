# use these functions to save/increment shifts, comparisons, accesses, swaps
# stats are saved in the form of [shifts, comparisons, accesses, swaps]
# Note that a swap counts as 2 shifts and 4 accesses,
# and a comparisons between 2 list elements 2 accesses

def addShift(stats, value=1, accesses=1):
    stats[0] += value
    stats[2] += accesses


def addComparison(stats, value=1, accesses=0):
    stats[1] += value
    stats[2] += accesses


def addAccess(stats, value=1):
    stats[2] += value


def addSwap(stats, value=1, accesses=4, shifts=2):
    stats[3] += value
    stats[0] += shifts
    stats[2] += accesses
