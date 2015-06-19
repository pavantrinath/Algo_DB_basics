def merger(l1,l2):
    if l1[-1] <= l2[0]:
        l3 = l1+ l2
        return l3
    m = len(l1)
    n = len(l2)
