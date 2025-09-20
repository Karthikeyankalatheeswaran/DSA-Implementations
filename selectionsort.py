array = [450,47,23425,775,2288,44,2,78,323,57]

def selectionsort(array):
    length = len(array)
    for i in range(length):
        min = i
        temp = array[i]
        for j in range(i+1,length):
            if array[j] < array[min]:
                min = j
        array[i] = array[min]
        array[min] = temp
    return array

print(selectionsort(array))

