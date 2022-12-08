# Create test lists (long, short, inverted, only a few elements wrong,
# Run each sorting algorithm on the lists
# Collect shifts/comparisons and running time
import random
import time

from SortingAlgorithms._helper_functions.quicksort import quicksort
from SortingAlgorithms.hybrid_quicksort import hybrid_quicksort
from SortingAlgorithms.flashsort import flashsort
from SortingAlgorithms.introsort import introsort
from SortingAlgorithms.shellsort import shellsort
from SortingAlgorithms._helper_functions.heapsort import heapsort
from SortingAlgorithms._helper_functions.insertionsort import insertionsort


def createList(n):
    return [random.randrange(0, n) for i in range(n)]


def scrambled(n):
    listAlmostSorted = [i for i in range(n)]
    # every swap changes 2 elements to be in the wrong spot. Moving 40 Elements to wrong position:
    for i in range(0, 1000):
        random_element = random.randrange(0, n)
        random_spot = random.randrange(0, n)
        listAlmostSorted[random_element], listAlmostSorted[random_spot] = \
            listAlmostSorted[random_spot], listAlmostSorted[random_element]
    return listAlmostSorted


# create test lists:
def createTestLists():
    # create lists:
    print("creating test lists...")

    testlists = [
        # main testing lists:
        ("list100", createList(100)),
        ("list1000", createList(1000)),
        ("list10000", createList(10000)),
        ("list100000", createList(100000)),
        ("list250000", createList(250000)),
        ("list500000", createList(500000)),
        ("list750000", createList(750000)),
        ("list1000000", createList(1000000))
        #
        # Other Lists:
        # ("list5", createList(5)),
        # ("list15", createList(15)),
        # ("list20", createList(20)),
        # ("list30", createList(30)),
        # ("list40", createList(40)),
        # ("list50", createList(50)),
        # ("list60", createList(60)),
        # ("list70", createList(70)),
        # ("list200", createList(200)),
        # ("list5000", createList(5000)),
        # ("list15000", createList(15000)),
        # ("list50000", createList(50000))
        # ("list1500000", createList(1500000))
        # ("list2000000", createList(2000000))
        #
        # Almost sorted lists:
        # ("list100AlmostSorted", scrambled(100)),
        # ("list1000AlmostSorted", scrambled(1000)),
        # ("list10000AlmostSorted", scrambled(10000)),
        # ("list100000AlmostSorted", scrambled(100000)),
        # ("list250000AlmostSorted", scrambled(250000)),
        # ("list500000AlmostSorted", scrambled(500000)),
        # ("list750000AlmostSorted", scrambled(750000)),
        # ("list1000000AlmostSorted", scrambled(1000000))
    ]

    print("test lists created!\n")
    return testlists


def runSort(sorting_algorithm, arr, stats):
    if sorting_algorithm == "hybrid_quicksort":
        hybrid_quicksort(arr=arr, threshold=30, stats=stats)
        return

    if sorting_algorithm == "flashsort":
        flashsort(arr, stats)
        return

    if sorting_algorithm == "introsort":
        introsort(arr, stats=stats, threshold=30)
        return

    if sorting_algorithm == "shellsort":
        shellsort(arr, stats)
        return

    if sorting_algorithm == "heapsort":
        heapsort(arr=arr, stats=stats)
        return

    if sorting_algorithm == "insertionsort":
        insertionsort(arr=arr, stats=stats)
        return

    if sorting_algorithm == "quicksort":
        quicksort(arr=arr, stats=stats)
        return

    print("algorithm ", sorting_algorithm, "doesn't exist")
    exit()


# available sorting algorithms: hybrid_quicksort, flashsort, introsort, shellsort, (heapsort, quicksort, insertionsort)
def testSorts(sorting_algorithms: list, repeats=1):
    lists = createTestLists()

    # create empty data list:
    data = [[sorting_algorithms[i], [[lists[j][0], [[0] for k in range(repeats)]] for j in range(len(lists))]] for i in
            range(len(sorting_algorithms))]

    # run each algorithm on each list. Optionally repeat multiple times
    for run in range(repeats):
        # create new test lists for each repeat
        lists = createTestLists()

        algorithm_nr = 0
        for algorithm in sorting_algorithms:
            list_nr = 0
            for testList in lists:
                # create name for list if not given:
                if type(testList) is list:
                    testList = tuple("custom list with" + len(testList) + "elements", testList)
                    print(testList)

                testListName = testList[0]
                arr = testList[1][:]

                # sort list using given sorting algorithm
                print("sorting", testListName, "using", algorithm, "...")

                # initialize stats. Stats are in the form of [shifts, comparisons, accesses]
                stats = [0, 0, 0, 0]

                # Run the algorithm and measure the runtime
                start_time = time.time()
                runSort(algorithm, arr, stats)
                end_time = time.time()

                # check if list is sorted
                if arr != sorted(testList[1]):
                    print("ERROR, List is not sorted")

                    wrong = []
                    # Find all wrong Elements and return their expected value
                    for i in range(len(arr)):
                        print("testing", i)
                        if arr[i] != sorted(testList[1])[i]:
                            wrong = wrong + [i]
                            print("i = ", i, "expected: ", sorted(testList[1])[i], "got: ", arr[i])
                    print("done checking")
                    for elem in wrong:
                        print("i = ", elem, "expected: ", sorted(testList[1])[elem], "got: ", arr[elem])
                    if wrong == []:
                        print("no errors!")
                    exit()

                # Stats:
                shifts = stats[0]
                comparisons = stats[1]
                accesses = stats[2]
                swaps = stats[3]
                sortTime = end_time - start_time

                data[algorithm_nr][1][list_nr][1][run] = [sortTime, shifts, comparisons, accesses, swaps]
                print("sorted", len(arr), "elements! Time: ", sortTime)
                print("shifts: ", shifts)
                print("comparisons: ", comparisons)
                print("List accesses: ", accesses)
                print("swaps: ", swaps)
                print("")
                list_nr += 1
            algorithm_nr += 1

    # for each algorithm and for each list, calculate average of data points
    for i in range(len(sorting_algorithms)):
        for j in range(len(lists)):
            listRuns = data[i][1][j][1]
            average = [(sum(x) / repeats) for x in zip(*listRuns)]
            minimum = [min(x) for x in zip(*listRuns)]
            maximum = [max(x) for x in zip(*listRuns)]
            data[i][1][j][1] += [("average", average)]
            data[i][1][j][1] += [("minimum elements", minimum)]
            data[i][1][j][1] += [("maximum elements", maximum)]

    return data


def showData(data):
    # for every sorting algorithm
    for i in data:
        # print the algorithms name
        print(i[0])
        # print all the data for each list
        """
        for j in range(0, len(i[1])):
            print(i[1][j])
        print("")
        # print only the average, min, max for each list
        for j in range(0, len(i[1])):
            print(i[1][j][0], i[1][j][1][-3:])
        """
        # print the data in a way so it can be used to create a graph easier
        averageTime = "Average Time: "
        minTime = "Minimum Time: "
        maxTime = "Maximum time: "
        shifts = "Average Shifts: "
        comparisons = "Average Comparisons: "
        accesses = "Average Accesses: "
        swaps = "Average swaps: "

        for j in range(0, len(i[1])):
            averageTime += i[1][j][0] + " " + str(i[1][j][1][-3][1][0]) + " "
            minTime += i[1][j][0] + " " + str(i[1][j][1][-2][1][0]) + " "
            maxTime += i[1][j][0] + " " + str(i[1][j][1][-1][1][0]) + " "
            shifts += i[1][j][0] + " " + str(i[1][j][1][-3][1][1]) + " "
            comparisons += i[1][j][0] + " " + str(i[1][j][1][-3][1][2]) + " "
            accesses += i[1][j][0] + " " + str(i[1][j][1][-3][1][3]) + " "
            swaps += i[1][j][0] + " " + str(i[1][j][1][-3][1][4]) + " "

        print("")
        print(averageTime)
        print(minTime)
        print(maxTime)
        print(shifts)
        print(comparisons)
        print(accesses)
        print(swaps)
        print("")
        print("")


# output = testSorts(["quicksort", "heapsort", "hybrid_quicksort", "introsort", "flashsort", "shellsort"], repeats=10)
output = testSorts(["insertionsort"], repeats=1)

showData(output)
