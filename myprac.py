list1 = [3,2,6,7,1]
val = 10

def summer(arr,k):
    buff = []
    output = []

    for num in arr:
        target = k - num
        if target not in buff:
            buff.append(num)

        else:
            output.append((min(num,target),max(num,target)))

    for i in output:
        print i

summer(list1,val)

def sumperms(arr,k,cache=[]):
    s = sum(cache)
    if s == k:
        print cache,k

    if s >= k:
        return
    for i in range(len(arr)):
        n = arr[i]
        rem = arr[i+1:]
        sumperms(rem,k,cache + [n])

sumperms([3,9,8,4,5,7,10],15)

def permu(word):
    if len(word) <= 1:
        return word

    subset = permu(word[1:])
    first_char = word[0]
    result = []
    for i in subset:
        for i in range(len(subset)):
            result.append(subset[i:]+str(first_char)+subset[:i])
    return result


def isNumber(s):

    try:
        i = float(s)
    except ValueError,TypeError:
        return False

    return True

print isNumber("231")
print isNumber("abbc")
print permu("abc")
