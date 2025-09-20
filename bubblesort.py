array = [450,47,23425,775,2288,44,2,78,323,57]

def bubblesort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]


bubblesort(array)
print(array)