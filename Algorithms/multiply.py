class MultiplyLargeIntegers:
    def __init__(self, number_one, number_two):
        self.one = str(number_one)
        self.two = str(number_two)

    def multiply(self):
        if len(self.one) == len(self.two):
            if len(self.one) % 2 == 0 and len(self.two) % 2 == 0:
                n = len(self.one)
                a_one, a_zero = int(self.one[:len(self.one) // 2]), int(self.one[len(self.one) // 2:])
                b_one, b_zero = int(self.two[:len(self.two) // 2]), int(self.two[len(self.two) // 2:])
                return int((a_one * b_one) * pow(10, n) + (a_one * b_zero + a_zero * b_one) * pow(10, n / 2) + (
                        a_zero * b_zero))
        return -1


test = MultiplyLargeIntegers(1234567898765432123456, 1234567898765432123456)
print(test.multiply())
