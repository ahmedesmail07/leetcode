class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[-i]:
                return False
            elif x == x[::-1]:
                return True
            else:
                return False