# unordered list search
def find_item_unordered(item, itemlist):
    for i in range(0, len(items)):
        if item == itemlist[i]:
            return i
    return None


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(find_item_unordered(23, items))

# ordered list


def binarysearch(item, itemlist):
    listsize = len(itemlist)-1
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        midPt = (lowerIdx+upperIdx) // 2
        if itemlist[midPt] == item:
            return midPt
        if item > itemlist[midPt]:
            lowerIdx = midPt+1
        else:
            upperIdx = midPt - 1
    return None


items = [6, 8, 19, 20, 23, 41, 49, 53, 56]
print(binarysearch(23, items))
