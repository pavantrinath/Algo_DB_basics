import unittest

def contigsum(list):
    current = total = list[0]
    for i in list[1:]:
        current = max(current+i, i)
        total = max(total,current)
    return total

class Mytest(unittest.TestCase):
     
    def test(self):
        self.assertEqual(contigsum([2,-8,3,-2,4,-10]), 5)
    
if __name__ == '__main__':
    unittest.main()    
    