class Solution:
    def isHappy(self, n: int) -> bool:
        # using set to prevent the cycle 
        seen = set()
        while n not in seen:
            seen.add(n)
            sqr_sum = 0
            while n > 0 :
                # getting the last digit of the number 
                sqr_sum += (n%10) ** 2
                # the first digit by using floor function
                # floor(19/10) == floor(1.9) == 1
                n = floor(n/10)
            if sqr_sum == 1:
                return True
            n = sqr_sum
        return False