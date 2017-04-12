import unittest

class unitest(unittest.TestCase):
    def testIsArithmetic(self):
        A = [1,2,3]
        self.assertEqual(Solution().numberOfArithmeticSlices(A),1);
    def testNotArithmetic(self):
        A = [1,2,4]
        self.assertEqual(Solution().numberOfArithmeticSlices(A),0);

class Solution():
    def numberOfArithmeticSlices(self, A):
        diff = None
        count = 0
        for x in range(1,len(A)):
            if diff is not None and (A[x]-A[x-1]) == diff:
                count += 1
            diff = A[x]-A[x-1]
        return count

if __name__ == '__main__':
    unittest.main()
