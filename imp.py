def findmergedinterval(list):
    sorter = (sorted(list))
    sorted_list = iter(sorter)
    finallist =[]

    for time in sorted_list:
        start_time = time[0]
        end_time = time[1]
        new_time = sorted_list.next()
        new_start = new_time[0]
        new_end = new_time[1]
        if new_start <= end_time :
                 new_tuple = min(start_time,new_start), max(end_time,new_end)
                 finallist.append(new_tuple)
        else:
                finallist.append(time)




    print finallist



thelist = [(1,3),(2,4),(5,7),(6,8),(10,12)]
findmergedinterval(thelist)














thelist = [(1,3), (2,4), (5,7), (6,8), (10,12)]
print findmergedinterval(thelist)
