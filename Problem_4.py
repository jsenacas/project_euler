class Problem_4:
    def solution(self):
        maximumPalindrome = 0
        for i in range(100, 999):
            for j in range(100, 999):
                result = i * j
                if self.isPalindrome(result):
                    if result > maximumPalindrome:
                        maximumPalindrome = result
        return maximumPalindrome

    def isPalindrome(self, n):
        return str(n) == str(n)[::-1]
