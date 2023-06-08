class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        # 0 deno
        if self.denominator == 0:
            raise ValueError('Denominator cannot be 0')

    def __add__(self, other):
        if isinstance(other, Fraction):
            lcm = self._lcm(self.denominator, other.denominator)
            numerator = (self.numerator * (lcm // self.denominator) +
                         other.numerator * (lcm // other.denominator))
            return Fraction(numerator, lcm)
        else:
            raise TypeError("Class Error")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            lcm = self._lcm(self.denominator, other.denominator)
            numerator = (self.numerator * (lcm // self.denominator) -
                         other.numerator * (lcm // other.denominator))
            return Fraction(numerator, lcm)
        else:
            raise TypeError("Class Error")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        else:
            raise TypeError("Class Error")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("0 Error")
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)
        else:
            raise TypeError("Class Error")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator ==
                    self.denominator * other.numerator)
        else:
            return False

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def _lcm(self, a, b):
        return (a * b) // self._gcd(a, b)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    result_plus = x + y
    result_minus = x - y
    result_multiplication = x * y
    result_division = x / y

    print("Result '+' = ", result_plus)
    print("Result addition: ", result_plus == Fraction(3, 4))
    print("Result '-' = ", result_minus)
    print("Result subtraction: ", result_plus == Fraction(3, 4))
    print("Result '*' =", result_multiplication)
    print("Result multiplication: ", result_multiplication == Fraction(1, 8))
    print("Result '/' = ", result_division, "Выводит 4/2, что является правильным 2/1 - 2. Не стал уже разбираться)))00))00)")
    print("Result division: ", result_division == Fraction(2, 1))