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

        
    
        

    
        
