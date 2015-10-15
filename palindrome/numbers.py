try:
    xrange
except NameError:
    xrange = range


class PalindromeNumber(object):
    """This class generates palindrome numbers.

    Examples:
        >>> palindromes = PalindromeNumber(max_number=3)
        >>> [x for x in palindromes.palindrome_numbers_generator()]
        [0, 1, 2, 3]
        >>> palindromes = PalindromeNumber(max_number=-1)
        Traceback (most recent call last):
            ...
        ValueError: max_number must be > 0"""

    def __init__(self,  max_number=1000000):
        if max_number < 0:
            raise ValueError('max_number must be > 0')
        self.max_number = max_number

    @staticmethod
    def is_palindrome(s):
        """Check whether a string is palindrome"""
        s = str(s)
        for i in xrange(len(s)):
            first = s[i]
            last = s[-i-1]
            if first != last:
                return False
        return True

    def exception_handler(self, number, exc):
        """Check whether the generated number is bigger than,
        max_number. Raise the desired exception."""
        try:  # one-digits numbers have wrapping zeros i.e. 010->1
            if int(number.strip('0')) > self.max_number:
                raise exc
        except ValueError:
            # Corner case: number is '000'
            if 0 > self.max_number or exc is ValueError:
                raise exc

    def build_palindrome(self, symmetry, center='', exc=None,
                         rtype=lambda x: int(x)):
        """Build a generic palindrome number with length > 1"""
        symmetry = str(symmetry)
        center = str(center)
        palindrome = symmetry
        if center:
            palindrome += center
        palindrome += symmetry[::-1]
        if exc:
            self.exception_handler(palindrome, exc)
        return rtype(palindrome)

    @staticmethod
    def _onedigit_exceptions(number_string, palindrome_length):
        """Handle one-digit number corner cases.
        Return integer version of the palindrome otherwise.
        - '000' -> '' -> 0
        - 9 -> next number will be longer i.e. 11"""
        palindrome = number_string.strip('0')
        if palindrome == '':
            palindrome = 0
        palindrome = int(palindrome)
        if palindrome == 9:
            palindrome_length += 1
        return palindrome, palindrome_length

    def palindrome_numbers_generator(self):
        """Generate palindrome numbers not bigger than max_number"""
        palindrome_length = 1
        palindrome = 0
        while palindrome <= self.max_number:

            palindrome_length_level = int(palindrome_length / 2)
            start_range = int(10**(palindrome_length_level - 1))
            end_range = max(10, 10**palindrome_length_level)

            for symmetry in xrange(start_range, end_range):
                symmetry = str(symmetry)
                length_is_even = palindrome_length % 2 == 0

                if length_is_even:
                    palindrome = self.build_palindrome(symmetry,
                                                       exc=StopIteration)
                    yield palindrome
                else:
                    for center in xrange(0, 10):
                        palindrome = self.build_palindrome(symmetry,
                                                           center=str(center),
                                                           exc=StopIteration,
                                                           rtype=lambda x: str(x))
                        palindrome, palindrome_length = self._onedigit_exceptions(
                            palindrome, palindrome_length)
                        yield palindrome
            palindrome_length += 1

    def __repr__(self):
        return '{}(max_number={})'.format(self.__class__.__name__,
                                          self.max_number)

    def __eq__(self, other):
        is_similar_type = isinstance(other, self.__class__)
        has_equal_attributes = self.max_number == other.max_number
        return has_equal_attributes and is_similar_type
