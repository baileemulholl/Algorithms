# Bubble Sort Performance: O(n^2)
def bubbleSort(unsortedData):
    for i in range(len(unsortedData)-1, 0, -1):
        for j in range(i):
            if unsortedData[j] > unsortedData[j+1]:
                temp = unsortedData[j]
                unsortedData[j] = unsortedData[j+1]
                unsortedData[j+1] = temp
    return unsortedData

# Merge Sort Performance: O(nlogn)


def mergeSort(unsortedData):
    if len(unsortedData) > 1:
        mid = len(unsortedData) // 2
        leftarr = unsortedData[:mid]
        rightarr = unsortedData[mid:]

        # recursively break down arrays
        mergeSort(leftarr)
        mergeSort(rightarr)

        i = 0  # index for left array
        j = 0  # index for right array
        k = 0  # index for merged array

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                unsortedData[k] = leftarr[i]
                i += 1
            else:
                unsortedData[k] = rightarr[j]
                j += 1
            k += 1

        # add left array values if any left
        while i < len(leftarr):
            unsortedData[k] = leftarr[i]
            i += 1
            k += 1
        # add right array values if any left
        while j < len(rightarr):
            unsortedData[k] = rightarr[j]
            j += 1
            k += 1
    return unsortedData

# Quicksort Performance: O(nlogn), worst case O(n^2) - generally better than Mergesort, but can be worse
# Performs in place, doesn't use extra memory


def quickSort(unsortedData, first, last):
    if first < last:
        # caclulate split point
        pivotIdx = partition(unsortedData, first, last)

        # sort two partitions
        quickSort(unsortedData, first, pivotIdx-1)
        quickSort(unsortedData, pivotIdx+1, last)


def partition(unsortedData, first, last):
    # first item is the pivot value
    pivot = unsortedData[first]
    lower = first+1
    upper = last

    # search for the crossing point
    done = False
    while not done:
        # advance lower index
        while lower <= upper and unsortedData[lower] <= pivot:
            lower += 1
        # advance upper index
        while unsortedData[upper] >= pivot and upper >= lower:
            upper -= 1
        # if two indexes cross, found split point
        if upper < lower:
            done = True
        else:
            temp = unsortedData[lower]
            unsortedData[lower] = unsortedData[upper]
            unsortedData[upper] = temp
    # after finding split point, exchange pivot value
    temp = unsortedData[first]
    unsortedData[first] = unsortedData[upper]
    unsortedData[upper] = temp

    # return split point index
    return upper


unsortedData1 = [0, 6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(bubbleSort(unsortedData1))
unsortedData2 = [0, 6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(mergeSort(unsortedData2))
unsortedData3 = [0, 6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
quickSort(unsortedData3, 0, len(unsortedData3)-1)
print(unsortedData3)
