class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        elif isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = denominator
        elif isinstance(numerator, str):
            separated = numerator.split("/")
            if len(separated) != 2 or separated[0].isalpha():
                self.numerator = 0
                self.denominator = 0
            else:
                self.numerator = int(separated[0])
                self.denominator = int(separated[1])
        else:
            self.numerator = 0
            self.denominator = 0

    def gcd(a, b):
        # If any of the parameters is 0, returns 0
        if a == 0 or b == 0:
            return 0
        # If any of the parameters is not an integer, returns an 'Invalid input' statement
        if int(a) != a or int(b) != b:
            return "Invalid input. Use integers only."
        # If both parameters are valid, identifies which parameter is bigger and which is smaller
        else:
            smaller = 0
            if a > b:
                smaller = b
            else:
                smaller = a
            # Creates a list for the common factors of the parameters
            commonFactors = []
            # Checks which integers from 1 to the smaller number is a common factor of both parameters and adds that integer to the list
            for number in range(1, smaller+1):
                if a % number == 0 and b % number == 0:
                    commonFactors.append(number)
            # Sorts the elements of the common factors list, returns the first element
            commonFactors.sort()
            return commonFactors[0]

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass