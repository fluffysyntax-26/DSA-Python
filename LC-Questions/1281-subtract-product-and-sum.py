class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_sum = 0
        digit_product = 1

        while n > 0:
            digit = n % 10
            
            digit_sum += digit
            digit_product *= digit

            n //= 10

        return digit_product - digit_sum