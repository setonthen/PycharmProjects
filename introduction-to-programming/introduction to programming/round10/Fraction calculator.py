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


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a


def main():
    command=input('> ')
    fracs={}
    while command!='quit':
        if command == 'add':
            fr = input('Enter a fraction in the form integer/integer: ')
            name = input('Enter a name: ')
            fracs[name] = fr
            command = input('> ')
        elif command=='print':
            to_print=input('Enter a name: ')
            if to_print not in fracs:
                print('Name '+to_print+' was not found')
                command = input('> ')
            else:
                print(to_print+' = '+fracs[to_print])
                command = input('> ')
        elif command=='list':
            if fracs=={}:
                command = input('> ')
            else:
                arraged=sorted(fracs)
                for x in arraged:
                    print(x + ' = ' + fracs[x])
                command = input('> ')
        elif command=='*':
            a=input('1st operand: ')
            if a not in fracs:
                print('Name '+a+' was not found')
                command = input('> ')
            else:
                b = input('2nd operand: ')
                if b not in fracs:
                    print('Name ' + b + ' was not found')
                    command = input('> ')
                else:
                    first_fr=fracs[a].split('/')
                    second_fr=fracs[b].split('/')
                    frac1=Fraction(int(first_fr[0]),int(first_fr[1]))
                    frac2=Fraction(int(second_fr[0]),int(second_fr[1]))
                    product=frac1.multiply(frac2)
                    simp=product.simplify()
                    prn=simp.return_string()
                    print(fracs[a]+' * '+fracs[b]+' = '+product.return_string())
                    print('simplified '+prn)
                    command = input('> ')



        else:
            print('Unknown command!')
            command = input('> ')
    if command == 'quit':
        print('Bye bye!')
main()
