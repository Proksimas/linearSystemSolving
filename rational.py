def gcd( integer1, integer2):
    """
    Return the value of the gcd between the integer: integer1 and integer2
    """

    gcd = 1

    for i in reversed(range(2, min(integer1, integer2) + 1)):
        if integer1 % i == 0 and integer2 % i == 0:
            gcd = i
            break
        

    return gcd

class Rational:
    """
    Class representative a rational number with a numerator and a denominator
    """
    def __init__(self, numerator, denominator):

        self.numerator = numerator
        self.denominator = denominator

    def multiply (self, rational2):
        """
        Multiply the current rational with another and return the result
        """

        num = self.numerator * rational2.numerator
        den = self.denominator * rational2.denominator

        return Rational(num, den)

    def add(self, rational2):
        """
        Add the current rational with another and return the result
        """

        num = self.numerator * rational2.denominator +\
              rational2.numerator * self.denominator

        den = self.denominator * rational2.denominator

        return Rational(num, den)

    def reverse(self):
        """
        Return the reverse value of the current rational
        """

        return Rational(self.denominator, self.numerator)

    def divided(self, rational2):
        """
        Divided the current rational by another
        """

        return self.multiply(rational2.reverse())

    def simplify(self):
        """
        Simplify the current rational
        """

        gcd_simple = gcd(self.numerator, self.denominator)

        self.numerator /= gcd_simple
        self.denominator /= gcd_simple

        

if __name__ == "__main__":

    assert(gcd(1, 5) == 1)
    assert(gcd(5, 10) == 5)
    assert(gcd(37, 7) == 1)

    a = Rational(2, 3)
    b = Rational(5, 3)
    c = Rational(7, 3)

    print (a.add(b))
    
        

        
    
        

    
        
