def klar(arr,k):
    left = []
    right = []
    pivotList = []
    pivot = arr[0]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
                
        else:
            pivotList.append(i)
                
    

    return 1














thelist = [7,2,3,4,1,9,8]
print klar(thelist,3)
