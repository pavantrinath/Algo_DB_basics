#given an integer array, output all pairs that
#sum up to a specific value k.

arr = [1,2,3,4,6]
targ = 5
seen = set()
output = set()
for num in arr: 
    target=targ-num 
    if target not in seen: 
        seen.add(num)
    else: 
        output.add( (min(num, target), max(num, target)) ) 
print '\n'.join( map(str, list(output)) ) 