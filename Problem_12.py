class Problem_12:
    def solution(self):
        index = 0
        incremental = 1

        while True:
            index += incremental
            result = self.calculateDivisors(index)

            if result > 500:
                return index

            incremental += 1


    def calculateDivisors(self, n):
        # return sum([2 for i in range(1, int(n ** (1/2)) + 1) if n % i == 0])
        for i in range(1, int(n ** (1/2)) + 1):
            if n % i == 0:
                return 2
            if n == int(n ** (1/2)) * int(n ** (1/2)):
                return 1


# //This solution does not work for perfect squares

print(Problem_12().solution())
