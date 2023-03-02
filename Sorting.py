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


unsortedData1 = [0, 6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(bubbleSort(unsortedData1))
unsortedData2 = [0, 6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(mergeSort(unsortedData2))
