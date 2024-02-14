class Solution:
    def isHappy(self, n: int) -> bool:
        number_set = set()
        number_set.add(n)
        while n != 1:
            n_string = str(n)
            new_number = 0
            for digit in n_string:
                new_number += int(digit) ** 2
            n = new_number
            if n in number_set:
                return False
            else:
                number_set.add(n)

        return True
