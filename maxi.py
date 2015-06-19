def get_max(list):
    max = None
    for i in list:
        if (i > max):
            max = i
    return max

list1 = [-1,-5,-3,-4]

print max(list1)       
        