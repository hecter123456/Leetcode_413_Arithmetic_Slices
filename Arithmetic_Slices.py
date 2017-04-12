import unittest

class unitest(unittest.TestCase):
    def testIsArithmetic(self):
        A = [1,2,3]
        self.assertEqual(Solution().numberOfArithmeticSlices(A),1);
    def testNotArithmetic(self):
        A = [1,2,4]
        self.assertEqual(Solution().numberOfArithmeticSlices(A),0);
    def testContinuousArithmetic(self):
        A = [1,2,3,4]
        self.assertEqual(Solution().numberOfArithmeticSlices(A),3);
    def testSecondContinuousArithmetic(self):
        A = [1,2,3,4,5,6]
        self.assertEqual(Solution().numberOfArithmeticSlices(A),10);
    def testArithmetic(self):
        A = [1,2,3,5,6,8,9,10,11,13,15]
        self.assertEqual(Solution().numberOfArithmeticSlices(A),5);

class Solution():
    def numberOfArithmeticSlices(self, A):
        diff = None
        continuous = 0
        ans = 0
        for x in range(1,len(A)):
            if diff is not None and (A[x]-A[x-1]) == diff:
                continuous += 1
                ans += continuous
            else:
                continuous = 0
                diff = A[x]-A[x-1]
        return ans

if __name__ == '__main__':
    unittest.main()
