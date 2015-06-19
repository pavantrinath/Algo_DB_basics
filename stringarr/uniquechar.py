def unique(s):
    return len(set(s)) == len(s)

def rev(s):
    return s[::-1]


def replacer(s):
    word = s.replace(" ","%20")
    return word

    
    

print unique("pavan")
print rev("pavan")        
print replacer("Mr pavan trinath")
