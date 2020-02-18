class Problem21:
    def __init__(self):
        self.amicable = []
        self.dictionary = {}

    def findDivisors(self, n):
        total = 1
        for i in range(2, int(n/2) + 1):
            if n % i == 0:
                total += i
        return total

    def printDivisors(self, n):
        divisors = [i for i in range(2, int(n/2) + 1) if n % i == 0]
        divisors.append(1)
        return divisors

    def solution(self):
        for i in range(2, 10000):
            divisor = self.findDivisors(i)
            self.dictionary[i] = divisor
            if divisor in self.dictionary.keys():
                if self.dictionary[divisor] == i:
                    if self.dictionary[divisor] == divisor:
                        continue
                    else: self.amicable.append((divisor, i))
        total = 0
        for k, v in self.amicable:
            total += k + v
        return total

print(Problem21().solution())
