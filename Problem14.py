class Problem14:

    def recursiveCall(self, n):
        if n == 1:
            return 1
        else:
            if self.isEven(n):
                return 1 + self.recursiveCall(self.ifEven(n))
            else: return 1 + self.recursiveCall(self.ifOdd(n))


    def Solution(self):
        memo = {}
        rangeOfNumber = range(2, 1000001)
        count = 1
        maximumNumber = 0
        maximum = 0

        for i in rangeOfNumber:
            if i in memo:
                count += memo[i]
            else:
                memo[i] = self.recursiveCall(i)
            count += 1
            if memo[i] > maximumNumber:
                maximumNumber = memo[i]
                maximum = i
        print(maximum)





    def isEven(self, n):
        return n % 2 == 0

    def ifEven(self, n):
        return n/2

    def ifOdd(self, n):
        return 3 * n + 1


Problem14().Solution()