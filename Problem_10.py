class Problem_10:
    def __init__(self):
        self.count = 2

    def solution(self, n):
        for i in range(3, n, 2):
            self.count += self.is_prime(i)
        return self.count

    def is_prime(self, n):
        if n == 2: return 2
        if n % 2 == 0: return 0
        for i in range(3, int(n ** (1/2) + 1), 2):
            if n % i == 0: return 0
        return n