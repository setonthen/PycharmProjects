class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of 
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format 
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                     abs(self.__denominator))
    def simplify(self):
        divisor=greatest_common_divisor(self.__numerator,self.__denominator)
        self.__numerator=self.__numerator//divisor
        self.__denominator=self.__denominator//divisor


    def complement(self):
        frac=Fraction(self.__numerator,self.__denominator)
        if frac.__numerator * frac.__denominator < 0:
            frac.__numerator=-frac.__numerator
        elif frac.__numerator * frac.__denominator > 0:
            frac.__numerator=-frac.__numerator
        return frac

    def reciprocal(self):
        frac = Fraction(self.__numerator, self.__denominator)
        a=frac.__numerator
        frac.__numerator=frac.__denominator
        frac.__denominator=a
        return frac

    def multiply(self,frac):
        fr=Fraction(self.__numerator,self.__denominator)
        a=frac.__numerator
        b=frac.__denominator
        fr.__numerator=fr.__numerator*a
        fr.__denominator=fr.__denominator*b
        return fr

    def divide(self,frac):
        fr = Fraction(self.__numerator, self.__denominator)
        a = frac.__numerator
        b = frac.__denominator
        fr.__numerator=fr.__numerator*b
        fr.__denominator=fr.__denominator*a
        return fr

    def add(self,frac):
        fr = Fraction(self.__numerator, self.__denominator)
        a = frac.__numerator
        b = frac.__denominator
        c=fr.__numerator
        d=fr.__denominator
        fr.__denominator=b*d
        fr.__numerator=(a*d+c*b)
        return fr

    def deduct(self,frac):
        fr = Fraction(self.__numerator, self.__denominator)
        a = frac.__numerator
        b = frac.__denominator
        c = fr.__numerator
        d = fr.__denominator
        fr.__denominator = b * d
        fr.__numerator = (c * b - a * d)
        return fr

    def __lt__(self, other):
        a=self.__numerator
        b=self.__denominator
        c=other.__numerator
        d=other.__denominator
        return (a/b)<(c/d)

    def __str__(self):
        return str(self.__numerator)+'/'+str(self.__denominator)



def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a

