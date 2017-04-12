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

class Solution():
    def numberOfArithmeticSlices(self, A):
        diff = None
        continuous = 0
        ans = 0
        for x in range(1,len(A)):
            if diff is not None and (A[x]-A[x-1]) == diff:
                continuous += 1
            else:
                ans += self.dp(continuous)
                diff = A[x]-A[x-1]
        ans += self.dp(continuous)
        return ans
    def dp(self,n):
        if(n is 0):
            return 0
        if(n is 1):
            return 1
        return self.dp(n-1)*2 - self.dp(n-2) +1

if __name__ == '__main__':
    unittest.main()
