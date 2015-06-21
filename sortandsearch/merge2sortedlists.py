def merger(a,b):
    l = []

    while a and b:
        if a[0] < b[0]:
            l.append(a.pop(0))

        else:
            l.append(b.pop(0))


        return l + a + b    

list1 = [1,2,3]
list2 = [3,4,5]
print merger(list1,list2)
