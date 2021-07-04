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
        frac=Fraction(self.__numerator,self.__denominator)
        divisor=greatest_common_divisor(frac.__numerator,frac.__denominator)
        frac.__numerator=frac.__numerator//divisor
        frac.__denominator=frac.__denominator//divisor
        return frac



def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a


def main():
    print('Enter fractions in the format integer/integer.')
    print('One fraction per line. Stop by entering an empty line.')
    frac_list=[]
    while True:
        frac=input()
        if frac=='':
            break
        splitted=frac.split('/')
        fr=Fraction(int(splitted[0]),int(splitted[1]))
        frac_list.append(fr)
    print('The given fractions in their simplified form:')
    for x in range(len(frac_list)):
        a=frac_list[x]
        b=a.simplify()
        orig=a.return_string()
        simp=b.return_string()
        print(orig+' = '+simp)

main()
