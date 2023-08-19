class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = "".join(map(str,digits))
        int_digit = int(str_digits)
        x = int_digit + 1
        x = str(x)
        new_digits = []
        for i in range(len(x)):
            new_digits.append(int(x[i]))
        return new_digits
        