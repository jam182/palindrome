from .numbers import PalindromeNumber


class DoubleBasePalindrome(PalindromeNumber):
    """This class provides sum of numbers tha are palindrome
    in both decimal and binary base

    Examples:
        >>> palindromes = DoubleBasePalindrome()
        >>> palindromes.sum_palindrome_numbers()
        872187"""

    @staticmethod
    def _binary(n):
        """Convert integer to binary in string format"""
        return '{0:b}'.format(n)

    @classmethod
    def is_double_base_palindrome(cls, n):
        """Check whether a number is palindrome in both
        decimal and binary base"""
        if n % 2 == 0:  # Only odd numbers can be valid
            return False
        if cls.is_palindrome(n) and cls.is_palindrome(cls._binary(n)):
            return True
        return False

    def double_base_palindrome_generator(self):
        """yield double base palindrome numbers
        not bigger than max_number"""
        for x in self.palindrome_numbers_generator():
            if self.is_double_base_palindrome(x):
                yield x

    def sum_palindrome_numbers(self):
        """Sum all palindrome numbers not bigger than max_number"""
        s = 0
        for x in self.double_base_palindrome_generator():
            s += x
        return s
