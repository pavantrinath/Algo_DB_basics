import unittest

def adder(arr1,arr2):
    arr3 = []
    
    if len(arr1) < 1:
        return arr2
    if len(arr2) < 1:
        return arr1
    
    
    zipped = zip(arr1,arr2)
    carry = 0

    for i in zipped[::-1]:
        val = (int(i[0])+int(i[1]))

        if carry+ val >= 10:
            arr3.append((carry +val) %10)
            carry = 1          
        
        else :
            arr3.append(carry+val)
            carry = 0
    
    return arr3[::-1]        
    

class Test(unittest.TestCase):
    
    def test(self):
        self.assertEqual(adder([3,4,7,8],[1,6,9,8]),[5,1,7,6])
        self.assertEqual(adder([1,2,3,4],[5,6,7,8]),[6,9,1,2])
        
if __name__ == '__main__':
    unittest.main()                                          
        


