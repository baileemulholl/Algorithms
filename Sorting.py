# Bubble Sort
# Performance: O(n^2)

def bubbleSort(unsortedData):
    for i in range(len(unsortedData)-1, 0, -1):
        for j in range(i):
            if unsortedData[j] > unsortedData[j+1]:
                temp = unsortedData[j]
                unsortedData[j] = unsortedData[j+1]
                unsortedData[j+1] = temp
    return unsortedData


unsortedData = [0, 6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
bubbleSort(unsortedData)
print("unsortedData", unsortedData)
