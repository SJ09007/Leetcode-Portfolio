class Solution(object):
    def digitSum(self, n):
        if n == 0:
            return 0
        return n % 10 + self.digitSum(n // 10)
    def digitProduct(self, n):
        if 0 <= n < 10:
            return n
        return (n % 10) * self.digitProduct(n // 10)

    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        check1 = self.digitSum(n) + self.digitProduct(n)
        return n % check1 == 0

        