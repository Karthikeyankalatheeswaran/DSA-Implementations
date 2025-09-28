import math

array = [450,47,23425,775,2288,44,2,78,323,57]

def mergesort(array):
    if len(array) == 1 :
        return array
    
    length = len(array)
    mid = math.floor(length / 2)
    left = array[:mid]
    right = array[mid:]
    
    return merge(mergesort(left),mergesort(right))
    

def merge(left,right):
    result = []
    leftIndex = 0
    rightIndex = 0
    
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex +=1
        else:
            result.append(right[rightIndex])  
            rightIndex +=1  
    
    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])
    
    
    print(left,right)
    return result

sorted_array = mergesort(array)
print(sorted_array)
