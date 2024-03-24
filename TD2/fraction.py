import math

EULER_CONSTANT = 0.5772


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        """Defines a fraction"""
        if type(numerator) is not int or type(denominator) is not int:
            # Check for correct types
            raise "Numerator or / and denominator is / are not integer"
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        """Overrides equality method"""
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return False

    def toString(self):
        """Return the correct format of a fraction"""
        return f"({self.numerator} / {self.denominator})"

    def mutiply(self, other_fraction):
        """Multiply two fractions"""
        return Fraction(self.numerator * other_fraction.numerator,
                        self.denominator * other_fraction.denominator
                        ).simplify()

    def add(self, other_fraction):
        """Add two fractions"""
        return Fraction(self.numerator * other_fraction.denominator +
                        other_fraction.numerator * self.denominator,
                        self.denominator * other_fraction.denominator
                        ).simplify()

    def simplify(self):
        """Simplify a fraction"""
        biggest_divisor = math.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // biggest_divisor,
                        self.denominator // biggest_divisor)


def compute_Hn(n: int):
    """Compute the nth term of the harmonic series"""
    frac = Fraction(1, 1)
    for i in range(2, n+1):  # We want the nth rank
        frac = frac.add(Fraction(1, i))
    return frac


def compute_leibniz_formula(n: int):
    """Compute the nth term of the leibniz formula"""
    frac = Fraction(1, 1)
    negative_sign = -1
    for i in range(3, n+1, 2):
        frac = frac.add(Fraction(negative_sign * 1, i))
        negative_sign *= -1
    return frac


if __name__ == "__main__":
    frac1 = Fraction(3, 4)
    print("My fraction is equal to", frac1.toString())

    frac2 = Fraction(5, 6)
    frac2.numerator
    assert frac1.mutiply(frac2) == Fraction(5, 8)
    assert frac1.add(frac2) == Fraction(19, 12)

    frac3 = Fraction(5, 15).simplify()
    assert frac3 == Fraction(1, 3)

    n = 10000
    # H10000 has too many digits to be printed
    print("H(10) = ", compute_Hn(10).toString())

    t = compute_Hn(n)
    temp = t.numerator / t.denominator
    h = math.log(n) + EULER_CONSTANT + 1/(2*n)

    print("Difference between H(n) - (log(n) + euler_constant + 1/2n) equals:"
          , temp - h)

    assert compute_leibniz_formula(5) == Fraction(13, 15)
    assert compute_leibniz_formula(7) == Fraction(76, 105)
