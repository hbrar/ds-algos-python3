import Implementation
import unittest

# class name can be arbitrary
class FibTest(unittest.TestCase):
    # FibTest is inheriting from class unittest.TestCase
    
    # Normal array
    arr1 = [3, 6, 4, 1, 9, 5]
    sortedArr1 = Implementation.iSort(arr1)
    expctArr1 = [1, 3, 4, 5, 6, 9]
    
    # Duplicates
    arr2 = [3, 6, 4, 1, 4, 9, 3]
    sortedArr2 = Implementation.iSort(arr2)
    expctArr2 = [1, 3, 3, 4, 4, 6, 9]
    
    # zeroes and ones
    arr3 = [0, 1, 0, 1, 0, 1, 0]
    sortedArr3 = Implementation.iSort(arr3)
    expctArr3 = [0, 0, 0, 0, 1, 1, 1]
    
    # 2 elements
    arr4 = [1,0]
    sortedArr4 = Implementation.iSort(arr4)
    expctArr4 = [0,1]
    
    # One element
    arr5 = [0]
    sortedArr5 = Implementation.iSort(arr5)
    expctArr5 = [0]
    
    # Empty array
    arr6 = []
    sortedArr6 = Implementation.iSort(arr6)
    expctArr6 = []
    
    # Reverse array
    arr7 = [4, 3, 2, 1]
    sortedArr7 = Implementation.iSort(arr7)
    expctArr7 = [1, 2, 3, 4]
    
    # Negative elements
    arr8 = [-4, 3, -12, 1, 0]
    sortedArr8 = Implementation.iSort(arr8)
    expctArr8 = [-12, -4, 0, 1 , 3]
    
    # The test cases are defined in this class by using methods
    # name of these methods is arbitrary, but has to start with test
    def testCases(self):
        self.assertEqual(isArrEq(self.sortedArr1,self.expctArr1), True)
        self.assertEqual(isArrEq(self.sortedArr2,self.expctArr2), True)
        self.assertEqual(isArrEq(self.sortedArr3,self.expctArr3), True)
        self.assertEqual(isArrEq(self.sortedArr4,self.expctArr4), True)
        self.assertEqual(isArrEq(self.sortedArr5,self.expctArr5), True)
        self.assertEqual(isArrEq(self.sortedArr6,self.expctArr6), True)
        self.assertEqual(isArrEq(self.sortedArr7,self.expctArr7), True)
        self.assertEqual(isArrEq(self.sortedArr8,self.expctArr8), True)
        
def isArrEq(sortedArr,expctArr):
    for i in range(len(expctArr)):
        if sortedArr[i] != expctArr[i]:
            return False
    return True

if __name__ == "__main__":
    unittest.main()
